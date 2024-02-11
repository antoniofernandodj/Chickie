from PySide6.QtCore import QObject
from src.config import settings
from PySide6.QtWidgets import QMessageBox
from typing import Optional
from contextlib import suppress

from src.domain.services import AuthService
import json
import httpx

with suppress(ImportError):
    from src.windows import MainWindow


class BaseController(QObject):
    window: 'MainWindow'

    def setup_auth_data(self):
        self.auth_service = AuthService()
        self.auth_data = self.auth_service.get_auth_data()
        self.loja = self.auth_service.get_loja_data()

    def get_request(self, endpoint: str):
        self.setup_auth_data()
        headers = {"Authorization": f"Bearer {self.auth_data.access_token}"}
        response = httpx.get(f"{settings.HOST}/{endpoint}", headers=headers)
        return response

    def post_request(self, endpoint: str, json: dict) -> httpx.Response:
        self.setup_auth_data()
        h = {"Authorization": f"Bearer {self.auth_data.access_token}"}
        j = json
        response = httpx.post(f"{settings.HOST}/{endpoint}", json=j, headers=h)
        return response

    def show_message(self, status: str, message: str) -> None:
        if status == "Success":
            QMessageBox.information(self.window, status, message)
        elif status == "Error":
            QMessageBox.critical(self.window, status, message)

    def handle_response(self, response: httpx.Response) -> Optional[str]:
        details = response.text
        if response.status_code == 200:
            r = str(json.loads(response.text)[0]["uuid"])
            return r

        elif response.status_code == 201:
            with suppress(Exception):
                return str(json.loads(response.text)["uuid"])

        elif response.status_code == 400:
            msg = f"Erro na requisição: dados inválidos. Detalhes: {details}"
            raise ValueError(msg)

        elif response.status_code == 401:
            raise ValueError("Erro de sessão: Sua sessão expirou!")

        elif response.status_code == 500:
            raise ValueError(f"Erro no servidor. Detalhes: {details}")

        else:
            msg = f"Erro desconhecido. Detalhes: {details}"
            self.show_message("Error", msg)

        return None
