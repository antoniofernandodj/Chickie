from src.domain.services import AuthService
from src.ui_models import HistoricoTableModel
from PySide6.QtGui import QCloseEvent
from contextlib import suppress


with suppress(ImportError):
    from src.windows import HistoricoDialog


class HistoricoController:
    def __init__(self, dialog: "HistoricoDialog"):
        self.dialog = dialog
        self.auth_service = AuthService()
        self.loja = self.auth_service.get_loja_data()
        table_view = self.dialog.view.table_view_historico
        self.historico_model = HistoricoTableModel(table_view)

    def setupUi(self):
        table_view = self.dialog.view.table_view_historico
        self.historico_model = HistoricoTableModel(table_view)
        self.dialog.view.table_view_historico.setModel(self.historico_model)
        self.historico_model.refresh(self.dialog.view.table_view_historico)

        self.dialog.closeEvent = self.on_dialog_close

    def on_dialog_close(self, arg__1: QCloseEvent):
        self.historico_model.clear()
        arg__1.accept()
