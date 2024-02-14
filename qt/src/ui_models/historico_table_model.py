from .base_pedidos_model import BasePedidosTableModel


class HistoricoTableModel(BasePedidosTableModel):
    reverse = True
    mode = True
