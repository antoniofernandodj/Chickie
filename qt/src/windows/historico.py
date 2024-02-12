from PySide6.QtWidgets import QDialog
from src.controllers import HistoricoController
from src.ui_models import HistoricoTableModel


class HistoricoDialog(QDialog):
    def __init__(self):
        from src.views.historico_ui import Ui_Dialog

        super().__init__()

        self.view = Ui_Dialog()
        self.view.setupUi(self)
        self.controller = HistoricoController(self)
        self.controller.setupUi()
