from PySide6.QtWidgets import QDialog
from src.controllers import PedidosController


class PedidosDialog(QDialog):
    def __init__(self):
        from src.views.pedidos_ui import Ui_Dialog

        super().__init__()

        self.view = Ui_Dialog()
        self.view.setupUi(self)
        self.controller = PedidosController(self)
        self.controller.setupUi()
