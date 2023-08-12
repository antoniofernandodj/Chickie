from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox
from typing import Optional
import json
import httpx


class BaseController(QObject):
    def getRequest(self, endpoint: str):
        headers = {
            "Authorization": f"Bearer {self.window.token}"  # type: ignore
        }
        response = httpx.get(
            f"http://localhost:8000/{endpoint}",
            headers=headers,
        )
        return response

    def postRequest(self, endpoint: str, json: dict) -> httpx.Response:
        headers = {
            "Authorization": f"Bearer {self.window.token}"  # type: ignore
        }
        response = httpx.post(
            f"http://localhost:8000/{endpoint}", json=json, headers=headers
        )
        return response

    def showMessage(self, status: str, message: str) -> None:
        if status == "Success":
            QMessageBox.information(
                self.window, status, message  # type: ignore
            )
        elif status == "Error":
            QMessageBox.critical(self.window, status, message)  # type: ignore

    def handleResponse(
        self, response: httpx.Response, successMessage: str = ""
    ) -> Optional[str]:
        if response.status_code == 200:
            r = str(json.loads(response.text)[0]["uuid"])
            return r

        elif response.status_code == 201:
            if successMessage:
                self.showMessage("Success", successMessage)
            # self.window.setupController()
            # with suppress(Exception):
            #     r = str(json.loads(response.text)["uuid"])
            #     return r

        elif response.status_code == 400:
            self.showMessage("Error", "Erro na requisição: dados inválidos.")
            raise ValueError

        elif response.status_code == 401:
            self.showMessage("Error", "Erro de sessão: Sua sessão expirou!")
            raise ValueError

        elif response.status_code == 500:
            self.showMessage("Error", "Erro no servidor.")
            raise ValueError

        else:
            self.showMessage("Error", "Erro desconhecido.")
        return None
