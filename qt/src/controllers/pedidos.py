from PySide6.QtWidgets import QMessageBox
from src.domain.services import AuthService, PedidoService
from src.ui_models import (
    PedidosTableModel,
    StatusListModel,
    ItensPedidoTableModel
)
from contextlib import suppress
import datetime


with suppress(ImportError):
    from src.windows import PedidosDialog


class PedidosController:
    def __init__(self, dialog: "PedidosDialog"):
        self.dialog = dialog
        self.auth_service = AuthService()
        self.loja = self.auth_service.get_loja_data()
        self.pedidos_model = PedidosTableModel()
        self.pedido_service = PedidoService()
        self.dialog.view.push_button_concluido.clicked.connect(self.concluido)
        self.pedidos_model = PedidosTableModel()
        self.status_model = StatusListModel()
        self.itens_model = ItensPedidoTableModel()
        self.dialog.view.table_view_itens_pedido.setModel(self.itens_model)

    def setupUi(self):
        self.dialog.view.table_view_pedidos.setModel(self.pedidos_model)
        self.dialog.view.combo_box_status.setModel(self.status_model)

        self.pedidos_model.set_size(
            self.dialog.view.table_view_pedidos,
            self.pedidos_model.sizes
        )

        cb = self.visualizar_pedido
        self.dialog.view.push_button_visualizar_pedido.clicked.connect(cb)
        self.dialog.view.table_view_pedidos.doubleClicked.connect(cb)

        cb = self.visualizar_pedidos
        self.dialog.view.push_button_pedidos.clicked.connect(cb)

    def visualizar_pedido(self):
        selected_items = self.dialog.view.table_view_pedidos.selectedIndexes()
        if not selected_items:
            return

        index = selected_items[0]
        if index.column() != 0:
            title = 'Aviso'
            text = 'Escolher linha ou id de pedido.'
            QMessageBox.warning(self.dialog, title, text)
            return

        pedido_uuid = self.pedidos_model.get(index)
        sizes, _ = self.itens_model.refresh(pedido_uuid)

        pedido = self.itens_model.get_pedido()

        args = (self.dialog.view.table_view_itens_pedido, sizes)
        self.itens_model.set_size(*args)

        frete = f'R${pedido.frete:.2f}'.replace('.', ',')
        total = f'R${pedido.total:.2f}'.replace('.', ',')

        fmt_data_hora = datetime.datetime \
            .fromisoformat(str(pedido.data_hora)) \
            .strftime('%d/%m/%Y %H:%M:%S')

        self.dialog.view.line_edit_data_hora.setText(fmt_data_hora)
        self.dialog.view.line_edit_celular.setText(str(pedido.celular))
        self.dialog.view.line_edit_frete.setText(frete)
        self.dialog.view.line_edit_total.setText(total)
        self.dialog.view.line_edit_status.setText(str(pedido.status_uuid))
        self.dialog.view.text_edit_comentarios.setText(str(pedido.comentarios))

        self.dialog.view.stackedWidget.setCurrentIndex(1)

    def visualizar_pedidos(self):
        self.dialog.view.stackedWidget.setCurrentIndex(0)

    def concluido(self):
        selected_items = self.dialog.view.table_view_pedidos.selectedIndexes()
        if not selected_items:
            return

        index = selected_items[0]
        if index.column() != 0:
            title = 'Aviso'
            text = 'Escolher linha ou id de pedido.'
            QMessageBox.warning(self.dialog, title, text)
            return

        status_code = self.pedidos_model.concluir(index)
        if status_code == 204:
            title = 'Sucesso'
            text = 'Pedido concluído com sucesso!'
            QMessageBox.information(self.dialog, title, text)
            self.pedidos_model.refresh()

        else:
            title = 'Erro'
            text = 'Erro na conclusão do pedido'
            QMessageBox.critical(self.dialog, title, text)
            return
