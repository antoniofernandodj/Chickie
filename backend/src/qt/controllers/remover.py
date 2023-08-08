from PySide6.QtWidgets import QApplication, QMainWindow
from contextlib import suppress

with suppress(ImportError):
    from qt.views.main import Ui_Chickie


class ControllerRemover:
    def __init__(
        self, view: "Ui_Chickie", app: QApplication, window: QMainWindow
    ):
        self.view = view
        self.app = app
        self.window = window

        self.view.actionRemoverCategoria.triggered.connect(
            self.removerCategoria
        )
        self.view.actionRemoverEntregador.triggered.connect(
            self.removerEntregador
        )
        self.view.actionRemoverFuncionario.triggered.connect(
            self.removerFuncionario
        )
        self.view.actionRemoverMetodoDePagamento.triggered.connect(
            self.removerMetodoDePagamento
        )
        self.view.actionRemoverZonaDeEntrega.triggered.connect(
            self.removerZonaDeEntrega
        )
        self.view.actionRemoverPreco.triggered.connect(self.removerPreco)
        self.view.actionRemoverProduto.triggered.connect(
            self.removerProduto
        )  #

    def removerCategoria(self):
        print("removerCategoria")

    def removerEntregador(self):
        print("removerEntregador")

    def removerFuncionario(self):
        print("removerFuncionario")

    def removerMetodoDePagamento(self):
        print("removerMetodoDePagamento")

    def removerZonaDeEntrega(self):
        print("removerZonaDeEntrega")

    def removerCliente(self):
        print("removerCliente")

    def removerPreco(self):
        print("removerPreco")

    def removerPedido(self):
        print("removerPedido")

    def removerProduto(self):
        print("removerProduto")
