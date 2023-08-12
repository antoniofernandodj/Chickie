from PySide6.QtWidgets import QMainWindow
from src.qt.controllers import LoginController


class LoginWindow(QMainWindow):
    def __init__(self, app):
        from src.qt.views.loginForm_ui import Ui_MainWindow

        super().__init__()
        self.app = app

        # View
        self.view = Ui_MainWindow()
        self.view.setupUi(self)

        self.controller = LoginController(
            view=self.view, app=self.app, window=self
        )

        self.controller.setup()
