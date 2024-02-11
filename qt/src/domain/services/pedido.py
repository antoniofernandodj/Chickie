from src.config import settings
from src.domain.data_models import PedidoGET
from .base import BaseService


class PedidoService(BaseService):
    base_url = f"{settings.HOST}/pedidos/"
    Model = PedidoGET
