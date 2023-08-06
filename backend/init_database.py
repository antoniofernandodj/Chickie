import asyncio
from src.infra.database.entities import Base
from src.infra.database.config import engine


async def create_database():
    from src.infra import database

    await database.config.init_database()
    Base.metadata.create_all(engine)


asyncio.run(create_database())
