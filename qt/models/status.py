import httpx
import json
from domain.models import Status
from domain.services import AuthService
from contextlib import suppress
from config import settings


with suppress(ModuleNotFoundError, ImportError):
    from windows import MainWindow  # type: ignore # noqa


class StatusModel:
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
        self.data = self.get_data()
        self.nomes = [item.nome for item in self.data]

    def refresh(self):
        self.data = self.get_data()

    def get_from_nome(self, nome: str):
        for item in self.data:
            if item.nome == nome:
                return item

    def get_data(self):
        response = httpx.get(
            f"{settings.HOST}/status/",
            headers={"Authorization": f"Bearer {self.token}"},
            params={"loja_uuid": self.loja_uuid},
        )
        responseJson = json.loads(response.text)
        return [Status(**statusData) for statusData in responseJson]
