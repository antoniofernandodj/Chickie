from PySide6.QtWidgets import QMainWindow
from src.ui_models.uf import UF
from src.controllers import MainController
from src.services import FileService as FS
from src.config import settings  # type: ignore


class MainWindow(QMainWindow):
    def __init__(self, app):
        from src.views.main_ui import Ui_MainWindow

        super().__init__()

        self.app = app

        self.view = Ui_MainWindow()
        self.view.setupUi(self)
        self.setupUI()

        if settings.STYLES:
            qss = FS.get('src/styles/main.qss')
            self.view.centralwidget.setStyleSheet(qss)

            qss = FS.get('src/styles/all.qss')
            self.view.tab_widget.setStyleSheet(qss)

            self.setStyleSheet(FS.get('src/styles/main-window.qss'))

        self.controller = MainController(self.view, self.app, self)
        self.controller.setup()

        self.view.action_sair.triggered.connect(self.app.exit)

    def setupUI(self):

        self.view.combo_box_uf_pedido.clear()
        self.view.combo_box_uf_cliente.clear()

        self.view.combo_box_uf_pedido.addItems([uf.name for uf in UF])
        self.view.combo_box_uf_cliente.addItems([uf.name for uf in UF])

        combo_box = self.view.combo_box_categoria_produto
        combo_box.clear()

        text = 'Escolha uma categoria de produto...'
        combo_box.addItem(text, userData=None)

        cb_produto_preco = self.view.combo_box_produto_preco
        cb_item_pedido = self.view.combo_box_item_pedido

        cb_produto_preco.clear()
        cb_item_pedido.clear()

        text = 'Escolha um produto...'
        cb_produto_preco.addItem(text, userData=None)
        cb_item_pedido.addItem(text, userData=None)
