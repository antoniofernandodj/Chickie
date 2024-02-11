from src.config import settings
from .base import BaseService
from src.domain.data_models import ProdutoGET
import httpx
import json


class LojaService(BaseService):
    base_url = f"{settings.HOST}/loja/"

    def get_produtos(self):
        url = self.base_url + "produtos/"
        response = httpx.get(url, headers=self.headers)
        response_json = json.loads(response.text)
        return [
            ProdutoGET(**produto_data) for produto_data
            in response_json['payload']
        ]
