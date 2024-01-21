from config import settings as s
from typing import Callable
from typing import Any
import asyncio
import aioamqp  # type: ignore
import pickle


class RMQService:
    def __init__(self):
        self.exchange_name = s.RABBITMQ_EXCHANGE_NAME
        self.credentials = dict(
            host=s.RABBITMQ_HOST,
            port=s.RABBITMQ_PORT,
            login=s.RABBITMQ_DEFAULT_USER,
            password=s.RABBITMQ_DEFAULT_PASS
        )

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()

    async def connect(self):
        print('Connecting...')
        self.transport, self.protocol = await aioamqp.connect(
            **self.credentials
        )
        print('Connected!')
        self.channel = await self.protocol.channel()
        print('Channel declared')
        await self.channel.queue_declare(s.RABBITMQ_QUEUE, durable=True)
        print('Queue declared')
        await self.channel.queue_bind(
            queue_name=s.RABBITMQ_QUEUE,
            exchange_name=self.exchange_name,
            routing_key=s.RABBITMQ_ROUTING_KEY
        )
        print('Queue binded!')

    async def send(self, payload: Any, headers: dict = {}):
        payload_bytes = pickle.dumps(payload)
        await self.channel.basic_publish(
            payload=payload_bytes,
            exchange_name=self.exchange_name,
            routing_key=s.RABBITMQ_ROUTING_KEY,
            properties={'headers': headers, 'delivery_mode': 2}
        )
        print('Message sent')

    async def start_consuming(self, callback: Callable):
        print('Listening...')
        while True:
            await self.channel.basic_consume(
                callback=callback,
                queue_name=s.RABBITMQ_QUEUE,
                no_ack=True
            )
            await asyncio.sleep(1)

    async def close(self):
        print('Closing')
        await self.channel.close()
        print('Closed')
