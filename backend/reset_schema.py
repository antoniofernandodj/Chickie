from src.infra.database_postgres.config import DatabaseConnectionManager
import asyncio


async def remover_schema(schema: str) -> None:
    sql = f"""
    DROP SCHEMA {schema} CASCADE;
    CREATE SCHEMA {schema};
    """

    async with DatabaseConnectionManager() as connection:
        cursor = await connection.cursor()
        r = await cursor.execute(sql)
        print({'r': r})

        cursor.close()

asyncio.run(remover_schema('public'))
