import json
from contextlib import suppress

from src.domain.data_models import Produto
from src.domain.services import AuthService, LojaService
from src.config import settings


with suppress(ModuleNotFoundError, ImportError):
    from windows import MainWindow  # type: ignore # noqa


class ProdutosModel:

    base_url = f"{settings.HOST}/produtos/"

    def __init__(self, window: "MainWindow"):
        self.window = window

        self.auth_service = AuthService()
        self.loja_service = LojaService()

        auth_data = self.auth_service.auth_data

        if auth_data is None:
            raise RuntimeError
        loja = auth_data.loja
        if loja is None:
            raise RuntimeError

        self.loja_uuid = loja.uuid
        self.token = auth_data.access_token
        self.data = self.get_data()
        self.nomes = [item.nome for item in self.data]

    def refresh(self):
        self.data = self.get_data()

    def get(self, uuid: str):
        for item in self.data:
            if item.uuid == uuid:
                return item

        raise ValueError('Nenhum item encontrado.')

    def get_data(self):
        response = self.loja_service.get_produtos()
        response_json = json.loads(response.text)
        return [
            Produto(**produto_data) for produto_data
            in response_json['payload']
        ]
