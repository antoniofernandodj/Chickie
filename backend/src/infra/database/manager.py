from config import settings as s
import aiopg


class DatabaseConnectionManager:
    CONNECTION_STRING_DB = "dbname={0} user={1} password={2} host={3}".format(
        s.POSTGRES_DATABASE_DEV,
        s.POSTGRES_USERNAME,
        s.POSTGRES_PASSWORD,
        s.POSTGRES_HOST,
    )

    CONNECTION_STRING = "user={0} password={1} host={2}".format(
        s.POSTGRES_USERNAME, s.POSTGRES_PASSWORD, s.POSTGRES_HOST
    )

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
