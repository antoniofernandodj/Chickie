from PySide6.QtWidgets import QMessageBox
from contextlib import suppress
import json
import httpx

with suppress(ImportError):
    from src.qt.views.loginForm_ui import Ui_MainWindow as LoginView
    from src.qt.windows import LoginWindow


class LoginController:
    def __init__(self, view: "LoginView", app, window: "LoginWindow"):
        self.host = "http://localhost:8000"
        self.view = view
        self.app = app
        self.window = window

    def setup(self):
        self.view.pushButtonEntrar.clicked.connect(self.login)

    def login(self):
        from src.qt.windows import MainWindow  # noqa

        login = self.view.lineEditLogin.text()
        senha = self.view.lineEditSenha.text()

        response = httpx.post(
            f"{self.host}/loja/login",
            data={"username": login, "password": senha},
        )

        if response.status_code != 200:
            QMessageBox.critical(
                self.window, "Login", "Credenciais Inválidas"
            )
            return

        jsonData = json.loads(response.text)
        accessToken, loja_uuid = (
            jsonData["access_token"],
            jsonData["uuid"],
        )
        QMessageBox.information(
            self.window, "Login", "Loja logada com sucesso!"
        )

        window = MainWindow(
            app=self.app, loja_uuid=loja_uuid, token=accessToken
        )
        window.show()
        self.window.close()
