from pydantic import BaseModel
from typing import Optional


class ItemPedido(BaseModel):
    __tablename__ = "itens_pedido"
    quantidade: int
    subtotal: float
    produto_uuid: str
    pedido_uuid: str
    loja_uuid: str
    uuid: Optional[str] = None
