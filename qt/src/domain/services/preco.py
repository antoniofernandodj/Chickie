from src.config import settings
from src.domain.data_models import Preco
from .base import BaseService
import httpx


class PrecoService(BaseService):

    base_url = f"{settings.HOST}/precos/"

    def save(self, preco: Preco):
        body = preco.model_dump()
        response = httpx.post(self.base_url, json=body, headers=self.headers)
        return response
