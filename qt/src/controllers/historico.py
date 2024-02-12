from src.domain.services import AuthService
from src.ui_models import HistoricoTableModel
from contextlib import suppress


with suppress(ImportError):
    from src.windows import HistoricoDialog


class HistoricoController:
    def __init__(self, dialog: "HistoricoDialog"):
        self.dialog = dialog
        self.auth_service = AuthService()
        self.loja = self.auth_service.get_loja_data()
        self.historico_model = HistoricoTableModel()
        self.dialog.finished.connect(self.delete)

    def setupUi(self):
        self.historico_model = HistoricoTableModel()
        self.dialog.view.table_view_historico.setModel(self.historico_model)
        self.historico_model.set_size(
            self.dialog.view.table_view_historico,
            self.historico_model.sizes
        )

    def delete(self):
        del self
        self = None  # noqa
