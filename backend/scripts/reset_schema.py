import sys
import os
from pathlib import Path
import asyncio

parent = str(Path(os.path.dirname(__file__)).parent)

sys.path.append(parent)

from src.infra.database_postgres.manager import (  # noqa
    DatabaseConnectionManager
)


async def remover_schema(schema: str) -> None:
    sql = f"""
    DROP SCHEMA {schema} CASCADE;
    CREATE SCHEMA {schema};
    """

    async with DatabaseConnectionManager() as connection:
        cursor = await connection.cursor()
        await cursor.execute(sql)

        cursor.close()

asyncio.run(remover_schema('public'))
