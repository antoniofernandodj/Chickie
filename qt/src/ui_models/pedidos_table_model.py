from PySide6.QtCore import QModelIndex, QPersistentModelIndex
from .base_pedidos_model import BasePedidosTableModel


class PedidosTableModel(BasePedidosTableModel):
    reverse = False
    mode = False

    @property
    def reverse_mode(self):
        return True

    def concluir(self, index: QModelIndex | QPersistentModelIndex):
        uuid = self.get(index)
        return self.pedidos_service.concluir_pedido(uuid)
