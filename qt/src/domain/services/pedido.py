from src.config import settings
from src.domain.data_models import PedidoPOST
from .base import BaseService
import httpx


class PedidoService(BaseService):

    base_url = f"{settings.HOST}/pedidos/"

    def save(self, pedido: PedidoPOST):
        body = pedido.model_dump()
        response = httpx.post(self.base_url, json=body, headers=self.headers)
        return response
