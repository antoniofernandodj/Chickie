from config import settings as s
import aiopg
import psycopg2   # noqa
from psycopg2 import sql   # noqa
from typing import Optional
from asyncio import Lock   # noqa
import traceback
import logging


class DatabaseConnectionManager:

    CONNECTION_STRING = "user={0} password={1} host={2}".format(
        s.POSTGRES_USERNAME, s.POSTGRES_PASSWORD, s.POSTGRES_HOST
    )

    def __init__(self, args: Optional[list] = None):
        self.CONNECTION_STRING_DB = self.get_connection_string_db(args)

    def get_connection_string_db(self, args: Optional[list]):
        if args is None:
            CONNECTION_STRING_DB = (
                "dbname={0} user={1} password={2} host={3}".format(
                    s.POSTGRES_DATABASE,
                    s.POSTGRES_USERNAME,
                    s.POSTGRES_PASSWORD,
                    s.POSTGRES_HOST,
                )
            )
            return CONNECTION_STRING_DB

        if "test" in [item.lower() for item in args]:
            CONNECTION_STRING_DB = (
                "dbname={0} user={1} password={2} host={3}".format(
                    "test",
                    s.POSTGRES_USERNAME,
                    s.POSTGRES_PASSWORD,
                    s.POSTGRES_HOST,
                )
            )
        else:
            CONNECTION_STRING_DB = (
                "dbname={0} user={1} password={2} host={3}".format(
                    s.POSTGRES_DATABASE,
                    s.POSTGRES_USERNAME,
                    s.POSTGRES_PASSWORD,
                    s.POSTGRES_HOST,
                )
            )
        return CONNECTION_STRING_DB

    @classmethod
    async def get_connection(cls):
        CONNECTION_STRING_DB = (
            "dbname={0} user={1} password={2} host={3}".format(
                s.POSTGRES_DATABASE,
                s.POSTGRES_USERNAME,
                s.POSTGRES_PASSWORD,
                s.POSTGRES_HOST,
            )
        )

        pool = await aiopg.create_pool(CONNECTION_STRING_DB)

        connection = await pool.acquire()
        yield connection
        connection.close()
        pool.close()

    async def __aenter__(self):
        self.pool = await aiopg.create_pool(self.CONNECTION_STRING_DB)
        self.connection = await self.pool.acquire()
        return self.connection

    async def __aexit__(
        self,
        exception_type,
        exception_value,
        traceback_object
    ):
        self.connection.close()
        self.pool.close()

        if exception_type is not None:
            print(traceback.print_tb(traceback_object))
            logging.exception(
                "Exception occurred",
                exc_info=(
                    exception_type,
                    exception_value,
                    traceback_object
                )
            )

    @classmethod
    async def create_database(cls, name):
        command = (
            f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{name}'"
        )
        async with aiopg.create_pool(cls.CONNECTION_STRING) as pool:
            async with pool.acquire() as connection:
                async with connection.cursor() as cursor:
                    await cursor.execute(command)
                    ret = []
                    async for row in cursor:
                        ret.append(row)
                    if ret == []:
                        command = f"CREATE DATABASE {name}"
                        await cursor.execute(command)

    @classmethod
    async def remove_database(cls, name):
        command = (
            f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{name}'"
        )
        async with aiopg.create_pool(cls.CONNECTION_STRING) as pool:
            async with pool.acquire() as connection:
                async with connection.cursor() as cursor:
                    await cursor.execute(command)

                    exists = await cursor.fetchone()
                    if exists:
                        name = f"DROP DATABASE {name}"
                        await cursor.execute(name)

                    cursor.close()
