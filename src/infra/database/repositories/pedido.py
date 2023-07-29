import asyncio
from src.schemas import Pedido
from src.infra.database.repositories import BaseRepositoryClass


class PedidoRepository(BaseRepositoryClass):

    def __init__(self, connection):
        super().__init__(connection=connection)
        self.__tablename__ = 'pedidos'
        self.lock = asyncio.Lock()
        self.model = Pedido
