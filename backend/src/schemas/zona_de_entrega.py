from pydantic import BaseModel
from typing import Optional


class ZonaDeEntrega(BaseModel):
    __tablename__ = "zonas_de_entrega"
    pedido_uuid: str
    metodo_pagamento: str
    uuid: Optional[str] = None
