import asyncio
from src.schemas import CategoriaProdutos
from src.infra.database.repositories import BaseRepositoryClass


class CategoriaProdutosRepository(BaseRepositoryClass):

    def __init__(self, connection):
        super().__init__(connection=connection)
        self.__tablename__ = 'categorias_de_produtos'
        self.lock = asyncio.Lock()
        self.model = CategoriaProdutos
