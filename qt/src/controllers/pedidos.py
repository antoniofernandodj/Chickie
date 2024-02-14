from PySide6.QtWidgets import QMessageBox, QTableView
from PySide6.QtGui import QCloseEvent
from PySide6.QtCore import QTimer, QThread, Signal
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


class RefreshWorker(QThread):
    finished = Signal()

    def __init__(
        self,
        pedidos_model: PedidosTableModel,
        table_view: QTableView
    ):
        super().__init__()
        self.pedidos_model = pedidos_model
        self.table_view = table_view

    def run(self):
        print('Non blocking operation...')
        self.pedidos_model.refresh(self.table_view)
        self.finished.emit()


class PedidosController:
    def __init__(self, dialog: "PedidosDialog"):
        self.dialog = dialog
        self.auth_service = AuthService()
        self.loja = self.auth_service.get_loja_data()
        self.pedido_service = PedidoService()
        self.dialog.view.push_button_concluido.clicked.connect(self.concluido)
        table_view = self.dialog.view.table_view_pedidos
        self.pedidos_model = PedidosTableModel(table_view)
        self.status_model = StatusListModel()

        self.itens_model = ItensPedidoTableModel(
            table_view=self.dialog.view.table_view_itens_pedido,
            pedido_uuid=None
        )
        self.dialog.view.table_view_itens_pedido.setModel(self.itens_model)

        self.worker = RefreshWorker(
            self.pedidos_model,
            self.dialog.view.table_view_pedidos
        )

    def setupUi(self):
        self.dialog.view.table_view_pedidos.setModel(self.pedidos_model)
        self.dialog.view.combo_box_status.setModel(self.status_model)

        self.pedidos_model.refresh(self.dialog.view.table_view_pedidos)

        cb = self.visualizar_pedido
        self.dialog.view.push_button_visualizar_pedido.clicked.connect(cb)
        self.dialog.view.table_view_pedidos.doubleClicked.connect(cb)

        cb = self.visualizar_pedidos
        self.dialog.view.push_button_pedidos.clicked.connect(cb)

        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh_pedidos)
        self.timer.start(5000)

        self.dialog.closeEvent = self.on_dialog_close

    def on_dialog_close(self, arg__1: QCloseEvent):
        self.timer.stop()
        self.pedidos_model.clear()
        arg__1.accept()

    def refresh_pedidos(self):

        # self.worker.finished.connect(self.worker.deleteLater)
        self.worker.start()

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
        table_view = self.dialog.view.table_view_itens_pedido
        self.itens_model.refresh(pedido_uuid, table_view)

        pedido = self.itens_model.get_pedido()

        frete = f'R${pedido.frete:.2f}'.replace('.', ',')
        total = f'R${pedido.total:.2f}'.replace('.', ',')
        status = str(pedido.status_uuid or 'Pedido Realizado')

        if isinstance(pedido.data_hora, str):
            truncated_data_hora = pedido.data_hora.split('.', 1)[0]
        else:
            raise TypeError

        fmt_data_hora = datetime.datetime \
            .fromisoformat(str(truncated_data_hora)) \
            .strftime('%d/%m/%Y %H:%M:%S')

        self.dialog.view.line_edit_data_hora.setText(fmt_data_hora)
        self.dialog.view.line_edit_celular.setText(str(pedido.celular))
        self.dialog.view.line_edit_frete.setText(frete)
        self.dialog.view.line_edit_total.setText(total)
        self.dialog.view.line_edit_status.setText(status)
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
            self.refresh_pedidos()

        else:
            title = 'Erro'
            text = 'Erro na conclusão do pedido'
            QMessageBox.critical(self.dialog, title, text)
            return
