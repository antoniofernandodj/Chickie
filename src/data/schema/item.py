from __future__ import annotations

from pydantic import BaseModel


class ItemDePedidoDados(BaseModel):
    quantidade: str
    subtotal: str
    produto_uuid: str
    pedido_uuid: str
    loja_uuid: str
