from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ItemPedido(BaseModel):
    quantidade: int
    subtotal: float
    produto_uuid: str
    pedido_uuid: str
    loja_uuid: str
    uuid: Optional[str] = None
