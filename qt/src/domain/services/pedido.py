from src.config import settings
from src.domain.data_models import PedidoGET
from .base import BaseService
from typing import Optional
import httpx


class PedidoService(BaseService):
    base_url = f"{settings.HOST}/pedidos/"
    Model = PedidoGET

    def concluir_pedido(self, uuid: Optional[str]):
        if uuid is None:
            return None
        url_request = self.base_url + f"concluir_pedido/{uuid}"
        response = httpx.patch(url_request, headers=self.headers)
        return response.status_code
