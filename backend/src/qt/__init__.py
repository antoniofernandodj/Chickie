from . import views  # noqa
from PySide6.QtWidgets import QMainWindow
from src.qt.controllers import Controller


class MainWindow(QMainWindow):
    def __init__(self, app):
        from src.qt.views.main_ui import Ui_Chickie

        super().__init__()

        self.app = app
        self.view = Ui_Chickie()
        self.view.setupUi(self)

        self.controller = Controller(
            view=self.view, app=self.app, window=self
        )
