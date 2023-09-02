from config import settings as s
import aiopg
import psycopg2
from psycopg2 import sql
from typing import Optional


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

    async def __aenter__(self):
        self.pool = await aiopg.create_pool(self.CONNECTION_STRING_DB)
        self.connection = await self.pool.acquire()
        return self.connection

    async def __aexit__(self, exception_type, exception_value, traceback):
        self.connection.close()
        self.pool.close()
        if exception_type and exception_value and traceback:
            print({"exception_type": exception_type})
            print({"exception_value": exception_value})
            print(traceback)

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


class SyncDatabaseConnectionManager:
    def __init__(self):
        self.connection_pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dbname=s.POSTGRES_DATABASE,
            user=s.POSTGRES_USERNAME,
            password=s.POSTGRES_PASSWORD,
            host=s.POSTGRES_HOST,
        )

    def __enter__(self):
        self.connection = self.connection_pool.getconn()
        self.connection.autocommit = True
        return self.connection

    def __exit__(self, exception_type, exception_value, traceback):
        if self.connection:
            self.connection_pool.putconn(self.connection)

    @classmethod
    def create_database(cls, name):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user=s.POSTGRES_USERNAME,
                password=s.POSTGRES_PASSWORD,
                host=s.POSTGRES_HOST,
            )
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(
                sql.SQL(
                    "SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"
                ),
                (name,),
            )
            exists = cursor.fetchone()
            if not exists:
                cursor.execute(
                    sql.SQL("CREATE DATABASE {}").format(sql.Identifier(name))
                )
        finally:
            if conn:
                conn.close()

    @classmethod
    def remove_database(cls, name):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user=s.POSTGRES_USERNAME,
                password=s.POSTGRES_PASSWORD,
                host=s.POSTGRES_HOST,
            )
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(
                sql.SQL(
                    "SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"
                ),
                (name,),
            )
            exists = cursor.fetchone()
            if exists:
                cursor.execute(
                    sql.SQL("DROP DATABASE {}").format(sql.Identifier(name))
                )
        finally:
            if conn:
                conn.close()
