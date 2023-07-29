import pika
import pickle
from config import settings as s
from typing import Callable, Optional
from pika.exceptions import AMQPConnectionError, ConnectionWrongStateError
from contextlib import suppress
from typing import Any
import logging


class RabbitMQPublisher:
    """
    Classe para envio de mensagens ao rabbitmq. Seu uso foi projetado
    para ser feito com gerenciadores de contexto

    Uso:
        with RabbitMQPublisher) as publisher:
            publisher.publish('Hello, RabbitMQ!')

    """

    def __init__(self, routing_key: str):
        self.__routing_key = routing_key
        self.__queue = s.RABBITMQ_QUEUE
        self.__exchange = s.RABBITMQ_EXCHANGE
        self.__host = s.RABBITMQ_HOST
        self.__port = s.RABBITMQ_PORT
        self.__username = s.RABBITMQ_DEFAULT_USER
        self.__password = s.RABBITMQ_DEFAULT_PASS
        self.__connection = self.__create_connection()
        self.__channel = self.__create_channel()

    def close(self):
        self.__connection.close()
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.__connection.close()
        except:
            pass

        
    def __create_connection(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            virtual_host='/',
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )
        
        connection = pika.BlockingConnection(connection_parameters)
        return connection

    def __create_channel(self):
        self.__channel = self.__connection.channel()
        self.__channel.exchange_declare(
            exchange=self.__exchange,
            exchange_type='direct',
            durable=True
        )
        logging.info(f"Exchange {self.__exchange} declarada com sucesso!")
        
        self.__channel.queue_bind(
            routing_key=self.__routing_key,
            exchange=self.__exchange,
            queue=self.__queue,
        )
        logging.info(f"Fila {self.__queue} vinculada com sucesso!")
        
        return self.__channel
    
    def send_message(self, body: Any, headers:Optional[dict]=None):
        if headers is None:
            self.__channel.basic_publish(
                exchange=self.__exchange,
                routing_key=self.__routing_key,
                body=pickle.dumps(body),
                properties=pika.BasicProperties(
                    delivery_mode=2
                )
            )
        else:
            self.__channel.basic_publish(
                exchange=self.__exchange,
                routing_key=self.__routing_key,
                body=pickle.dumps(body),
                properties=pika.BasicProperties(
                    delivery_mode=2,
                    headers=headers
                )
            )

        return True


class RabbitMQConsumer:
    def __init__(self, callback: Callable, routing_key: str):
        self.__exchange = s.RABBITMQ_EXCHANGE
        self.__host = s.RABBITMQ_HOST
        self.__port = s.RABBITMQ_PORT
        self.__username = s.RABBITMQ_DEFAULT_USER
        self.__password = s.RABBITMQ_DEFAULT_PASS
        self.__routing_key = routing_key
        self.__queue = s.RABBITMQ_QUEUE
        self.__callback = callback
        self.__channel = self.__create_channel()
        self._logger: logging.Logger = None
        
    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            virtual_host='/',
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        connection = pika.BlockingConnection(connection_parameters)
        channel = connection.channel()        
        
        channel.exchange_declare(
            exchange=self.__exchange,
            exchange_type='direct',
            durable=True
        )
        logging.info(f"Exchange {self.__exchange} declarada com sucesso!")
        
        channel.queue_declare(
            queue=self.__queue,
            durable=True
        )
        logging.info(f"Fila {self.__exchange} declarada com sucesso!")
        
        channel.queue_bind(
            routing_key=self.__routing_key,
            exchange=self.__exchange,
            queue=self.__queue,
        )
        logging.info(f"Fila {self.__queue} vinculada com sucesso!")
        
        logging.info(f"Consumindo...")
        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback
        )

        return channel

    def start(self):
        self._logger.info(f'RabbitMQ escutando em {self.__host}:{self.__port}...')
        self.__channel.start_consuming()
