from .base_pedidos_model import BasePedidosTableModel


class HistoricoTableModel(BasePedidosTableModel):
    def mode(self):
        return True
