from PySide6.QtWidgets import QMessageBox
from src.domain.services import AuthService
from src.ui_models import PedidosTableModel, StatusListModel
from contextlib import suppress


with suppress(ImportError):
    from src.windows import PedidosDialog


class PedidosController:
    def __init__(self, dialog: "PedidosDialog"):
        self.dialog = dialog
        self.auth_service = AuthService()
        self.loja = self.auth_service.get_loja_data()
        self.pedidos_model = PedidosTableModel()
        self.dialog.view.push_button_concluido.clicked.connect(self.concluido)
        self.pedidos_model = PedidosTableModel()
        self.status_model = StatusListModel()
        self.dialog.finished.connect(self.delete)

    def setupUi(self):
        self.dialog.view.table_view_pedidos.setModel(self.pedidos_model)
        self.dialog.view.combo_box_status.setModel(self.status_model)

        self.pedidos_model.set_size(
            self.dialog.view.table_view_pedidos,
            self.pedidos_model.sizes
        )

    def concluido(self):
        selected_items = self.dialog.view.table_view_pedidos.selectedIndexes()
        for index in selected_items:
            column = index.column()
            if column == 0:
                status_code = self.pedidos_model.concluir(index)
                if status_code == 204:
                    title = 'Sucesso'
                    text = 'Pedido concluído com sucesso!'
                    QMessageBox.warning(self.dialog, title, text)

                    self.pedidos_model.refresh()

                else:
                    title = 'Erro'
                    text = 'Erro na conclusão do pedido'
                    QMessageBox.critical(self.dialog, title, text)

                return

        title = 'Aviso'
        text = 'Escolher linha ou id de pedido.'
        QMessageBox.warning(self.dialog, title, text)

    def delete(self):
        del self
        self = None  # noqa
