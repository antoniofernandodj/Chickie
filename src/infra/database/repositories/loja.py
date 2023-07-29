import asyncio
from src.schemas import Loja
from src.infra.database.repositories import BaseRepositoryClass


class LojaRepository(BaseRepositoryClass):

    def __init__(self, connection):
        super().__init__(connection=connection)
        self.__tablename__ = 'lojas'
        self.lock = asyncio.Lock()
        self.model = Loja
