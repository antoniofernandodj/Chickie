from src.config import settings
from src.domain.data_models import ProdutoGET
from .base import BaseService


class ProdutoService(BaseService):
    base_url = f"{settings.HOST}/produtos/"
    Model = ProdutoGET
