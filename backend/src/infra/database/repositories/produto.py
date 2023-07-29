import asyncio
from src.schemas import Produto
from src.infra.database.repositories import BaseRepositoryClass


class ProdutoRepository(BaseRepositoryClass):

    def __init__(self, connection):
        super().__init__(connection=connection)
        self.__tablename__ = 'produtos'
        self.lock = asyncio.Lock()
        self.model = Produto
