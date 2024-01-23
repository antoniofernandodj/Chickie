import sys
import os
from pathlib import Path
import asyncio
from aiopg import create_pool
parent = str(Path(os.path.dirname(__file__)).parent)

sys.path.append(parent)

from src.infra.database_postgres import DSN  # type: ignore # noqa 


async def remover_schema(schema: str) -> None:
    sql = f"""
    DROP SCHEMA {schema} CASCADE;
    CREATE SCHEMA {schema};
    """

    async with create_pool(DSN) as pool:
        async with pool.acquire() as connection:
            async with connection.cursor() as cursor:
                cursor = await connection.cursor()
                await cursor.execute(sql)

asyncio.run(remover_schema('public'))
