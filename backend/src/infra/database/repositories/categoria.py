import asyncio
from src.schemas import Categoria
from src.infra.database.repositories import BaseRepositoryClass


class CategoriaRepository(BaseRepositoryClass):

    def __init__(self, connection):
        super().__init__(connection=connection)
        self.__tablename__ = 'categorias'
        self.lock = asyncio.Lock()
        self.model = Categoria
