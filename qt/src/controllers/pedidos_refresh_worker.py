from PySide6.QtWidgets import QTableView
from PySide6.QtCore import QThread, Signal
from src.ui_models import PedidosTableModel


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
        self.pedidos_model.refresh(self.table_view)
        self.finished.emit()
