from PySide6.QtWidgets import QMainWindow, QListWidgetItem
from src.ui_models.uf import UF
from src.controllers import MainController
from src.ui_models import CategoriasModel, ProdutosModel, StatusModel
from src.services import FileService
from __feature__ import snake_case, true_property  # type: ignore  # noqa


class MainWindow(QMainWindow):
    def __init__(self, app):
        from src.views.main_ui import Ui_MainWindow

        super().__init__()

        self.app = app

        self.categorias = CategoriasModel(self)
        self.produtos = ProdutosModel(self)
        self.status = StatusModel(self)
        self.items = []

        self.view = Ui_MainWindow()
        self.view.setupUi(self)
        self.setupUI()

        qss = FileService.get_text('src/styles/main.qss')
        self.view.centralwidget.style_sheet = qss

        self.controller = MainController(self.view, self.app, self)
        self.controller.setup()

        self.view.action_sair.triggered.connect(self.app.exit)

    def setupUI(self):
        self.view.combo_box_uf_pedido.clear()
        self.view.combo_box_uf_cliente.clear()

        self.view.combo_box_uf_pedido.add_items([uf.name for uf in UF])
        self.view.combo_box_uf_cliente.add_items([uf.name for uf in UF])

        combo_box = self.view.combo_box_categoria_produto
        combo_box.clear()

        text = 'Escolha uma categoria de produto...'
        combo_box.add_item(text, userData=None)
        for categoria in self.categorias.data:
            Item = QListWidgetItem
            combo_box.add_item(categoria.nome, userData=categoria)
            list_widget = self.view.list_widget_categorias_cadastradas
            list_widget.add_item(Item(categoria.nome))

        combo_box_produto_preco = self.view.combo_box_produto_preco
        combo_box_item_pedido = self.view.combo_box_item_pedido

        combo_box_produto_preco.clear()
        combo_box_item_pedido.clear()

        text = 'Escolha um produto...'
        combo_box_produto_preco.add_item(text, userData=None)
        self.view.combo_box_item_pedido.add_item(text, userData=None)
        for produto in self.produtos.data:
            combo_box_produto_preco.add_item(produto.nome, userData=produto)
            combo_box_item_pedido.add_item(produto.nome, userData=produto)
