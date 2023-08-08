from PySide6.QtWidgets import QApplication, QMainWindow
from contextlib import suppress

with suppress(ImportError):
    from qt.views.main import Ui_Chickie


class ControllerAtualizar:
    def __init__(
        self, view: "Ui_Chickie", app: QApplication, window: QMainWindow
    ):
        self.view = view
        self.app = app
        self.window = window

        self.view.actionAtualizarCategoria.triggered.connect(
            self.atualizarCategoria
        )
        self.view.actionAtualizarEntregador.triggered.connect(
            self.atualizarEntregador
        )
        self.view.actionAtualizarFuncionario.triggered.connect(
            self.atualizarFuncionario
        )
        self.view.actionAtualizarZonaDeEntrega.triggered.connect(
            self.atualizarZonaDeEntrega
        )
        self.view.actionAtualizarPreco.triggered.connect(
            self.atualizarPreco
        )  #
        self.view.actionAtualizarPedido.triggered.connect(
            self.atualizarPedido
        )

    def atualizarCategoria(self):
        print("atualizarCategoria")

    def atualizarEntregador(self):
        print("atualizarEntregador")

    def atualizarFuncionario(self):
        print("atualizarFuncionario")

    def atualizarMetodoDePagamento(self):
        print("atualizarMetodoDePagamento")

    def atualizarZonaDeEntrega(self):
        print("atualizarZonaDeEntrega")

    def atualizarCliente(self):
        print("atualizarCliente")

    def atualizarPreco(self):
        print("atualizarPreco")

    def atualizarPedido(self):
        print("atualizarPedido")
