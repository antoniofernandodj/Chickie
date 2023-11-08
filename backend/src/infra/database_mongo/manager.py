from config import settings as s
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient


class DatabaseConnectionManager:

    conn_str = '{prot}+{type}://{usr}:{psw}@{host}/?retryWrites={retry}&w={w}'.format(
        prot=s.MONGODB_PROTOCOL,
        type=s.MONGODB_CONNECTION_TYPE,
        usr=s.MONGODB_USERNAME,
        psw=s.MONGODB_PASSWORD,
        host=s.MONGODB_HOSTNAME_OR_DNS_SEEDLIST,
        retry=s.MONGODB_RETRY_WRITE,
        w=s.MONGODB_WRITE_CONCERN
    )

    def __init__(self, args: Optional[list] = None):
        self.args = args

    async def __aenter__(self):
        connection = AsyncIOMotorClient(DatabaseConnectionManager.conn_str)
        return connection

    async def __aexit__(self, exception_type, exception_value, traceback_object):
        if exception_type and exception_value and traceback_object:
            import traceback
            print({"exception_type": exception_type})
            print({"exception_value": exception_value})
            print(traceback.print_tb(traceback_object))

    @classmethod
    async def create_database(cls, name):
        async with cls() as connection:
            db = connection[name]
            return db

    @classmethod
    async def remove_database(cls, name):
        async with cls() as connection:
            await connection.drop_database(name)
