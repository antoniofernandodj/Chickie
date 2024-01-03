from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings
from contextlib import suppress
import traceback
import logging


class DatabaseConnectionManager:

    conn_str = settings.MONGODB_URI

    def __init__(self, args: Optional[list] = None):
        self.args = args

    async def __aenter__(self):
        cls = type(self)
        self.connection = AsyncIOMotorClient(cls.conn_str)
        return self.connection

    async def __aexit__(
        self, exception_type, exception_value, traceback_object
    ):
        if self.connection:
            with suppress(Exception):
                self.connection.close()

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
        async with cls() as connection:
            db = connection[name]
            return db

    @classmethod
    async def remove_database(cls, name):
        async with cls() as connection:
            await connection.drop_database(name)
