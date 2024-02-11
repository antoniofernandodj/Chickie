from src.config import settings
from src.domain.data_models import Preco
from .base import BaseService
import httpx
import json


class PrecoService(BaseService):
    base_url = f"{settings.HOST}/precos/"
    Model = Preco

    def get_precos_from_produto(self, produto_uuid):
        response = httpx.get(
            self.base_url,
            headers=self.headers,
            params={
                "loja_uuid": self.loja_data.uuid,
                'produto_uuid': produto_uuid
            },
        )
        response_json = json.loads(response.text)
        return [
            Preco(**produto_data) for produto_data
            in response_json
        ]
