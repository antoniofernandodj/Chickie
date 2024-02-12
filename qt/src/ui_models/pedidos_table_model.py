from PySide6.QtCore import QModelIndex, QPersistentModelIndex
from .base_pedidos_model import BasePedidosTableModel


class PedidosTableModel(BasePedidosTableModel):
    def mode(self):
        return False

    def concluir(self, index: QModelIndex | QPersistentModelIndex):
        uuid = self.get(index)
        return self.pedidos_service.concluir_pedido(uuid)
