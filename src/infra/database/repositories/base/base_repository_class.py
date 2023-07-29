from aiopg import Connection
import logging
from typing import Type, List, Optional
from uuid import uuid4
from asyncio import Lock
from pydantic import BaseModel
import base64
import bcrypt


class UserMixin:
    def authenticate(self, user: any, senha_usuario: str):
        hash_bytes = base64.b64decode(user.password_hash.encode('utf-8'))
        return bcrypt.checkpw(senha_usuario.encode('utf-8'), hash_bytes)


class BaseRepositoryClass:
    
    """
    Base class for a repository that handles database interactions using aiopg.

    Attributes:
        connection (Connection): The aiopg Connection to the database.
        model (Type): The model class associated with the repository.
        lock (asyncio.Lock): The asyncio Lock to ensure safety on
                            asynchronous queries to the database
    """
    
    def __init__(self, connection: Connection):
        """
        Initialize the BaseRepositoryClass with a database connection.

        Args:
            connection (Connection): The aiopg Connection to the database.
        """
        self.connection = connection
        self.model: Type
        self.lock: Lock
        self.__tablename__: str

    async def find_one(self, **kwargs) -> Optional[Type]:
        """
        Find a single record in the database based on the provided filters.

        Args:
            **kwargs: Keyword arguments representing the filter criteria.

        Returns:
            object: The instance of the model if found, or None if no records match the criteria.
        """
        async with self.lock:
            cursor = await self.connection.cursor()
            if kwargs:
                table = self.__tablename__
                columns, values = kwargs.keys(), kwargs.values()
                where_clause = ' AND '.join(
                    [f'{column} = %s' for column in columns]
                )
                where_values = list(values)
                query = f'SELECT * FROM {table} WHERE {where_clause};'
                logging.debug(f'Query: {query} {where_values}\n')
                await cursor.execute(query, where_values)
            else:
                query = f'SELECT * FROM {table}'
                await cursor.execute(query)
                
            result = await cursor.fetchone()
            if result:
                column_names = [column[0] for column in cursor.description]
                dict_result = dict(list(zip(column_names, result)))
                cursor.close()
                return self.model(**dict_result)
            
            cursor.close()

    async def find_all(self, **kwargs) -> List:
        """
        Find all records in the database based on the provided filters.

        Args:
            **kwargs: Keyword arguments representing the filter criteria.

        Returns:
            list: List of model instances matching the filter criteria.
        """
        cursor = await self.connection.cursor()
        async with self.lock:

            if kwargs:
                columns, values = kwargs.keys(), kwargs.values()
                where_clause = ' AND '.join([f'{column} = %s' for column in columns])
                where_values = list(values)
                query = f'SELECT * FROM {self.__tablename__} WHERE {where_clause};'
                logging.debug(f'Query: {query} {where_values}\n')
                await cursor.execute(query, where_values)
            else:
                query = f'SELECT * FROM {self.__tablename__}'
                await cursor.execute(query)
                
            column_names = [column[0] for column in cursor.description]
            results = await cursor.fetchall()

            response_dicts = [
                {key: value for key, value in zip(column_names, list(result))}
                for result in results
            ]
            
            response = [self.model(**item) for item in response_dicts if item]
                
            return response

    async def save(self, pydantic_model: BaseModel):
        """
        Save a new record or update an existing record in the database.

        Args:
            **kwargs (dict): Keyword arguments representing the data to save.

        Returns:
            str: The uuid of the saved instance.
        """
        kwargs = pydantic_model.model_dump()
        kwargs['uuid'] = str(uuid4())
        cursor = await self.connection.cursor()
        async with self.lock:
            
            table = self.__tablename__
            columns = list(kwargs.keys())
            values = list(kwargs.values())
            
            column_clause = ', '.join(columns)
            value_placeholder = ', '.join(['%s'] * len(columns))
            query = f'INSERT INTO {table} ({column_clause}) VALUES ({value_placeholder});'
            logging.info(f'Command: {query} {values}')
            await cursor.execute(query, values)
            cursor.close()
            return kwargs['uuid']

    async def update(self, item: object, data: dict={}):
        """
        Update the existing item in the database based on the provided data.

        Args:
            item (object): A model instance of a row in the database

            data (dict): A dictionary representing the data to update. The keys should be column names,
                        and the values should be the new values for the corresponding columns.

        Returns:
            int: The number of rows affected by the update operation.
        """
        async with self.lock:
            cursor = await self.connection.cursor()
            set_clause = ', '.join(
                [f'{column} = %s' for column in data.keys()]
            )
            values = list(data.values())
            query = f"UPDATE {self.__tablename__} SET {set_clause} WHERE uuid = '{item.uuid}';"
            logging.info(f'Command: {query} {values}')
            await cursor.execute(query, values)
            num_rows_affected = cursor.rowcount
            cursor.close()
            return num_rows_affected

    async def delete(self, item: object):
        """
        Delete a record from the database based on the provided item.

        Args:
            item (object): The model instance with the UUID of the row to delete.

        Returns:
            int: The number of rows affected by the delete operation (1 if successful, 0 if no record found).
        """
        async with self.lock:
            cursor = await self.connection.cursor()
            uuid = item.uuid
            query = f'DELETE FROM {self.__tablename__} WHERE uuid = %s;'
            logging.debug(f'Query: {query} {uuid}\n')
            await cursor.execute(query, (uuid,))

            num_rows_affected = cursor.rowcount

            cursor.close()
            return num_rows_affected
