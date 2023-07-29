import asyncio
from src.schemas import Preco
from src.infra.database.repositories import BaseRepositoryClass


class PrecoRepository(BaseRepositoryClass):

    def __init__(self, connection):
        super().__init__(connection=connection)
        self.__tablename__ = 'precos'
        self.lock = asyncio.Lock()
        self.model = Preco
