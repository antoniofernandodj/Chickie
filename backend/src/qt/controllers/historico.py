from PySide6.QtWidgets import QApplication, QMainWindow
from contextlib import suppress

with suppress(ImportError):
    from qt.views.main import Ui_Chickie


class ControllerHistorico:
    def __init__(
        self, view: "Ui_Chickie", app: QApplication, window: QMainWindow
    ):
        self.view = view
        self.app = app
        self.window = window

        self.view.actionHistorico.triggered.connect(
            self.historicoDeVendas
        )  # xxx

    def historicoDeVendas(self):
        print("historicoDeVendas")
