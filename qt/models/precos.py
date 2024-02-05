import httpx
import json
from domain.models import Preco
from domain.services import AuthService
from contextlib import suppress
from config import settings
from typing import List


with suppress(ModuleNotFoundError, ImportError):
    from windows import MainWindow  # type: ignore # noqa


class PrecosModel:

    base_url = f"{settings.HOST}/precos/"

    def __init__(self, window: "MainWindow"):
        self.window = window

        self.auth_service = AuthService()
        auth_data = self.auth_service.auth_data

        if auth_data is None:
            raise RuntimeError
        loja = auth_data.loja
        if loja is None:
            raise RuntimeError

        self.loja_uuid = loja.uuid
        self.token = auth_data.access_token
        self.data: List[Preco] = []
        self.nomes = [item.valor for item in self.data]

    def refresh(self, produto_uuid: str):
        self.data = self.get_data(produto_uuid=produto_uuid)

    def get_data(self, produto_uuid: str):
        response = httpx.get(
            self.base_url,
            headers={"Authorization": f"Bearer {self.token}"},
            params={
                "loja_uuid": self.loja_uuid,
                'produto_uuid': produto_uuid
            },
        )
        response_json = json.loads(response.text)
        return [
            Preco(**produto_data) for produto_data
            in response_json
        ]
