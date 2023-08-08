from PySide6.QtWidgets import QApplication, QMainWindow
from contextlib import suppress

with suppress(ImportError):
    from qt.views.main import Ui_Chickie


class ControllerSobre:
    def __init__(
        self, view: "Ui_Chickie", app: QApplication, window: QMainWindow
    ):
        self.view = view
        self.app = app
        self.window = window

        self.view.actionSobreOChickie.triggered.connect(self.sobre)
        self.view.actionObterAjuda.triggered.connect(
            self.obterAjuda
        )  # xxxxxxxx
        self.view.actionCompartilharIdeias.triggered.connect(
            self.compartilharIdeias
        )

    def obterAjuda(self):
        print("obterAjuda")

    def compartilharIdeias(self):
        print("Compartilhar ideia")

    def sobre(self):
        print("Sobre")
