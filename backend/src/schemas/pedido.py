from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Pedido(BaseModel):
    __tablename__ = "pedidos"
    data_hora: datetime
    status: str
    frete: float
    loja_uuid: str
    endereco_uuid: str
    uuid: Optional[str] = None
