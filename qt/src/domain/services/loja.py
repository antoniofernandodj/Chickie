from src.config import settings
from .base import BaseService
import httpx


class LojaService(BaseService):

    base_url = f"{settings.HOST}/loja/"

    def get_produtos(self):
        url = f"{self.base_url}produtos/"
        response = httpx.get(url, headers=self.headers)
        return response
