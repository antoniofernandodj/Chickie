from PySide6.QtWidgets import QMainWindow
from src.qt.controllers.novo import ControllerNovo
from src.qt.controllers.atualizar import ControllerAtualizar
from src.qt.controllers.remover import ControllerRemover
from src.qt.controllers.historico import ControllerHistorico
from src.qt.controllers.sobre import ControllerSobre


class Controller:
    def __init__(self, view, app, window: QMainWindow):
        self.view = view
        self.app = app

        self.controllerNovo = ControllerNovo(
            view=self.view, app=self.app, window=window
        )
        self.controllerNovo = ControllerNovo(
            view=self.view, app=self.app, window=window
        )
        self.controllerAtualizar = ControllerAtualizar(
            view=self.view, app=self.app, window=window
        )
        self.controllerRemover = ControllerRemover(
            view=self.view, app=self.app, window=window
        )
        self.controllerHistorico = ControllerHistorico(
            view=self.view, app=self.app, window=window
        )
        self.controllerSobre = ControllerSobre(
            view=self.view, app=self.app, window=window
        )
