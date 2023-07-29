from __future__ import annotations
from pydantic import BaseModel


class PedidoDados(BaseModel):
    status: str
    frete: str
    endereco: str
    loja_uuid: str