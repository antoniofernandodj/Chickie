import asyncio
from src.schemas import Endereco
from src.infra.database.repositories import BaseRepositoryClass


class EnderecoRepository(BaseRepositoryClass):

    def __init__(self, connection):
        super().__init__(connection=connection)
        self.__tablename__ = 'endereco'
        self.lock = asyncio.Lock()
        self.model = Endereco
