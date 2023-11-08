from src.infra.database_postgres.entities.endereco import UF
from PySide6.QtWidgets import QMainWindow
from src.qt.controllers import MainController
from src.qt.models import CategoriasModel, ProdutosModel, StatusModel
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, app, loja_uuid, token):
        from src.qt.views.main_ui import Ui_MainWindow

        super().__init__()
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.app = app

        self.loja_uuid = loja_uuid
        self.token = token

        self.categorias = CategoriasModel(self)
        self.produtos = ProdutosModel(self)
        self.status = StatusModel(self)
        self.items = []

        self.view = Ui_MainWindow()
        self.view.setupUi(self)
        self.setupUI()

        self.controller = MainController(
            view=self.view, app=self.app, window=self
        )

        self.controller.setup()

        self.view.actionSair.triggered.connect(self.app.exit)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mousePos = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.mousePos is not None and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.mousePos)

    def mouseReleaseEvent(self, event):
        self.mousePos = None

    def setupUI(self):
        self.view.comboBoxUFZonaEntrega.clear()
        self.view.comboBoxUFZonaEntrega.addItems([uf.name for uf in UF])

        self.view.comboBoxUFCliente.clear()
        self.view.comboBoxUFCliente.addItems([uf.name for uf in UF])

        self.view.comboBoxCategoriaProduto.clear()
        self.view.comboBoxCategoriaProduto.addItems(self.categorias.nomes)

        self.view.comboBoxProdutoPreco.clear()
        self.view.comboBoxProdutoPreco.addItems(self.produtos.nomes)

        self.view.comboBoxItemPedido.clear()
        self.view.comboBoxItemPedido.addItems(self.produtos.nomes)
