from PySide6.QtWidgets import QApplication, QMainWindow
from contextlib import suppress

with suppress(ImportError):
    from src.qt.views.main import Ui_Chickie


class ControllerNovo:
    def __init__(
        self, view: "Ui_Chickie", app: QApplication, window: QMainWindow
    ):
        self.view = view
        self.app = app
        self.window = window

        self.view.actionNovaCategoria.triggered.connect(self.novaCategoria)
        self.view.actionNovoEntregador.triggered.connect(self.novoEntregador)
        self.view.actionNovoFuncionario.triggered.connect(
            self.novoFuncionario
        )
        self.view.actionNovoMetodoDePagamento.triggered.connect(
            self.novoMetodoDePagamento
        )
        self.view.actionNovaZonaDeEntrega.triggered.connect(
            self.novaZonaDeEntrega
        )
        self.view.actionNovoCliente.triggered.connect(self.novoCliente)
        self.view.actionNovoPreco.triggered.connect(self.novoPreco)
        self.view.actionNovoPedido.triggered.connect(self.novoPedido)

    def novaCategoria(self):
        from src.qt.views.novaCategoria_ui import Ui_Chickie
        from src.qt.controllers import Controller

        self.view = Ui_Chickie()
        self.view.setupUi(self.window)
        self.controller = Controller(self.view, self.app, self.window)

    def novoEntregador(self):
        print("novoEntregador")

    def novoFuncionario(self):
        from src.qt.views.novoFuncionario_ui import Ui_Chickie
        from src.qt.controllers import Controller

        self.view = Ui_Chickie()
        self.view.setupUi(self.window)
        self.controller = Controller(self.view, self.app, self.window)

    def novoMetodoDePagamento(self):
        print("novoMetodoDePagamento")

    def novaZonaDeEntrega(self):
        print("novaZonaDeEntrega")

    def novoCliente(self):
        print("novoCliente")

    def novoPreco(self):
        print("novoPreco")

    def novoPedido(self):
        print("novoPedido")
