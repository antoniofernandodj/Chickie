from PySide6.QtWidgets import QMessageBox, QApplication
from src.domain.services import AuthService, InvalidCredentials
from src.services import CacheService
from contextlib import suppress
import httpx

with suppress(ImportError):
    from src.views.loginForm_ui import (  # tyep: ignore
        Ui_MainWindow as LoginView
    )
    from src.windows import LoginWindow


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
        if auth_data is None:
            return
        if auth_data.get('login'):
            self.view.line_edit_login.setText(auth_data['login'])
        if auth_data.get('senha'):
            self.view.line_edit_senha.setText(auth_data['senha'])
            self.view.check_box_armazenar_senha.setChecked(True)

    def login(self) -> None:
        from src.windows import MainWindow

        login = self.view.line_edit_login.text()
        senha = self.view.line_edit_senha.text()

        try:
            self.auth_service.login(login=login, senha=senha)

        except InvalidCredentials as error:
            QMessageBox.critical(self.window, "Login", str(error))
            return

        except httpx.ConnectError:
            title = "Erro de conexão"
            text = "Erro na coneção com a api"
            QMessageBox.critical(self.window, title, text)
            return

        title = "Login"
        text = "Login realizado com sucesso!"
        QMessageBox.information(self.window, title, text)

        if self.view.check_box_armazenar_senha.isChecked():
            CacheService.cache_login_data(login, senha)
        else:
            CacheService.cache_login_data(login)

        window = MainWindow(app=self.app)
        window.show()
        self.window.close()
