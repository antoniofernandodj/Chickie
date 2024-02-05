from PySide6.QtWidgets import QMessageBox, QApplication
from domain.services import AuthService, InvalidCredentials
from services import FileService
from typing import Optional
from contextlib import suppress
from __feature__ import snake_case, true_property  # type: ignore  # noqa
import httpx

with suppress(ImportError):
    from views.loginForm_ui import Ui_MainWindow as LoginView
    from windows import LoginWindow


class CacheService:
    @classmethod
    def get_last_login_data(cls):
        try:
            return FileService.get_json('auth.json')
        except Exception:
            return None

    @classmethod
    def cache_login_data(cls, login, senha: Optional[str] = None):
        try:
            if senha is not None:
                data = {'login': login, 'senha': senha}
            else:
                data = {'login': login}

            return FileService.set_json('auth.json', data)
        except Exception:
            return None


class LoginController:
    def __init__(
        self,
        view: "LoginView",
        app: "QApplication",
        window: "LoginWindow"
    ):
        self.view = view
        self.app = app
        self.window = window
        self.auth_service = AuthService()

    def setup(self):
        self.view.push_button_entrar.clicked.connect(self.login)
        auth_data = CacheService.get_last_login_data()
        if auth_data:
            if auth_data.get('login'):
                self.view.line_edit_login.text = auth_data['login']
            if auth_data.get('senha'):
                self.view.line_edit_senha.text = auth_data['senha']
                self.view.check_box_armazenar_senha.checked = True

    def login(self) -> None:
        from windows import MainWindow

        login: str = self.view.line_edit_login.text
        senha: str = self.view.line_edit_senha.text

        try:
            self.auth_service.login(login=login, senha=senha)

        except InvalidCredentials as error:
            QMessageBox.critical(self.window, "Login", str(error))
            return

        except httpx.ConnectError:
            title = "Erro de conexão"
            msg = "Erro na coneção com a api"
            QMessageBox.critical(self.window, title, msg)
            return

        title = "Login"
        msg = "Loja logada com sucesso!"
        QMessageBox.information(self.window, title, msg)

        if self.view.check_box_armazenar_senha.checked:
            CacheService.cache_login_data(login, senha)
        else:
            CacheService.cache_login_data(login)

        window = MainWindow(app=self.app)
        window.show()
        self.window.close()
