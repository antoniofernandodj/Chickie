from src.infra.database_postgres.handlers import (
    QueryHandler, CommandHandler
)
from typing import List, Any, Optional
from aiopg import Connection


class BaseService:

    query_handler: QueryHandler
    model: Any

    def __init__(self, connection: Connection):
        self.query_handler = QueryHandler(self.model, connection)
        self.cmd_handler = CommandHandler(connection)

    async def get(self, uuid: str) -> Optional[Any]:
        return await self.query_handler.find_one(uuid=uuid)

    async def get_all(self, **kwargs) -> List[Any]:
        return await self.query_handler.find_all(**kwargs)
