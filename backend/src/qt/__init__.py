from . import views  # noqa
from src.infra.database.entities.endereco import UF
from PySide6.QtWidgets import QMainWindow
from src.qt.controllers import Controller
from src.qt.models import CategoriasModel, ProdutosModel, StatusModel
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):
    def __init__(self, app):
        from src.qt.views.mainV2_ui import Ui_MainWindow

        super().__init__()
        self.app = app

        # Models
        self.loja_uuid = "472d657d-7ed4-4431-bee9-dc0ccea98c73"
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsb2phIiwiZXhwIjoxNjkxODE0MjI0fQ.pYim-SHvaoRTSUbyUz6Mmp5zaJZjsTsQnC-Ew6eyUPc"  # noqa

        self.categorias = CategoriasModel(self)
        self.produtos = ProdutosModel(self)
        self.status = StatusModel(self)

        # View
        self.view = Ui_MainWindow()
        self.view.setupUi(self)
        self.setupUI()

        # Controller
        self.controller = Controller(
            view=self.view, app=self.app, window=self
        )
        self.controller.categoriaCatastrada.connect(self.atualizarCategoria)
        self.controller.produtoCatastrado.connect(self.atualizarProduto)

        self.controller.setup()

    def setupController(self):
        self.controller.setup()

    @Slot(str)
    def atualizarCategoria(self, categoriaNome: str):
        self.categorias.refresh()
        categoria = self.categorias.getFromNome(categoriaNome)
        if categoria is None:
            return
        self.view.comboBoxCategoriaProduto.addItem(categoria.nome)

    @Slot(str)
    def atualizarProduto(self, produtoNome: str):
        self.produtos.refresh()
        produto = self.produtos.getFromNome(produtoNome)
        if produto is None:
            return

        self.view.comboBoxProdutoPreco.addItem(produto.nome)
        self.view.comboBoxItemPedido.addItem(produto.nome)

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
