from src.config import settings
from src.domain.data_models import ProdutoPOST
from .base import BaseService
import httpx


class ProdutoService(BaseService):

    base_url = f"{settings.HOST}/produtos/"

    def save(self, produto: ProdutoPOST):
        body = produto.model_dump()
        response = httpx.post(self.base_url, json=body, headers=self.headers)
        return response
