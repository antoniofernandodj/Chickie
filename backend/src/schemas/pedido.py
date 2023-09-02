from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Pedido(BaseModel):
    __tablename__ = "pedidos"
    data_hora: datetime
    status: str
    frete: float
    loja_uuid: str
    endereco_uuid: str
    uuid: Optional[str] = None


class ItemPedido(BaseModel):
    __tablename__ = "itens_pedido"
    quantidade: int
    subtotal: float
    produto_uuid: str
    pedido_uuid: str
    loja_uuid: Optional[str] = None
    uuid: Optional[str] = None


class PedidoItens(BaseModel):
    __tablename__ = "pedidos"
    data_hora: datetime
    status: str
    frete: float
    loja_uuid: str
    endereco_uuid: str
    uuid: Optional[str] = None
    itens_pedido: List[ItemPedido] = None

