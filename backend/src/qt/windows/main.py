from src.infra.database.entities.endereco import UF
from PySide6.QtWidgets import QMainWindow
from src.qt.controllers import MainController
from src.qt.models import CategoriasModel, ProdutosModel, StatusModel


class MainWindow(QMainWindow):
    def __init__(self, app, loja_uuid, token):
        from src.qt.views.main_ui import Ui_MainWindow

        super().__init__()
        self.app = app

        # Models
        self.loja_uuid = loja_uuid
        self.token = token

        self.categorias = CategoriasModel(self)
        self.produtos = ProdutosModel(self)
        self.status = StatusModel(self)

        # View
        self.view = Ui_MainWindow()
        self.view.setupUi(self)
        self.setupUI()

        # Controller
        self.controller = MainController(
            view=self.view, app=self.app, window=self
        )

        self.controller.setup()

    def setupController(self):
        self.controller.setup()

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
