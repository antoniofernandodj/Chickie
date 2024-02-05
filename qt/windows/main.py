from models.uf import UF
from PySide6.QtWidgets import QMainWindow, QFileDialog, QListWidgetItem
from controllers import MainController
from models import CategoriasModel, ProdutosModel, StatusModel
from services import FileService
from __feature__ import snake_case, true_property  # type: ignore  # noqa


class MainWindow(QMainWindow):
    def __init__(self, app):
        from views.main_ui import Ui_MainWindow

        super().__init__()

        self.app = app

        self.categorias = CategoriasModel(self)
        self.produtos = ProdutosModel(self)
        self.status = StatusModel(self)
        self.items = []

        self.view = Ui_MainWindow()
        self.view.setupUi(self)
        self.setupUI()

        qss = FileService.get_text('styles/main.qss')
        self.view.centralwidget.style_sheet = qss

        self.controller = MainController(self.view, self.app, self)
        self.controller.setup()

        self.view.action_sair.triggered.connect(self.app.exit)

    def setupUI(self):
        self.view.comboBox.clear()
        self.view.combo_box_uf_cliente.clear()

        self.view.comboBox.add_items([uf.name for uf in UF])
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

        text = 'Escolha um produto...'
        combo_box_produto_preco = self.view.combo_box_produto_preco
        combo_box_item_pedido = self.view.combo_box_item_pedido

        combo_box_produto_preco.clear()
        combo_box_item_pedido.clear()

        combo_box_produto_preco.add_item(text, userData=None)
        self.view.combo_box_item_pedido.add_item(text, userData=None)
        for produto in self.produtos.data:
            combo_box_produto_preco.add_item(produto.nome, userData=produto)
            combo_box_item_pedido.add_item(produto.nome, userData=produto)

        callback = self.show_file_dialog
        self.view.push_button_escolher_imagem_produto.clicked.connect(callback)

    def show_file_dialog(self):
        formats = [
            'Images (*.png *.jpg *.jpeg *.bmp *.gif)',
            'PNG (*.png)',
            'JPG (*.jpg)',
            'JPEG (*.jpeg)',
            'bitmap (*.bmp)',
            'GIF (*.gif)'
        ]
        filters = ';;'.join(formats)
        caption = 'Escolha a imagem'
        file_path, _ = QFileDialog.get_open_file_name(
            self, filter=filters, selectedFilter=formats[0], caption=caption
        )

        self.view.label_produto_image_filename.text = file_path
