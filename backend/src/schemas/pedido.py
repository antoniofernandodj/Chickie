from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .item_pedido import ItemPedido

class Pedido(BaseModel):
    __tablename__ = "pedidos"
    data_hora: datetime
    status: str
    frete: float
    loja_uuid: str
    endereco_uuid: str
    uuid: Optional[str] = None

    class Config:
        json_schema_extra = {
            'example': {
                'data_hora': 'datetime',
                'status': 'str',
                'frete': 'float',
                'loja_uuid': 'str',
                'endereco_uuid': 'str'
            }
        }


class PedidoItens(BaseModel):
    __tablename__ = "pedidos"
    data_hora: datetime
    status: str
    frete: float
    loja_uuid: str
    endereco_uuid: str
    uuid: Optional[str] = None
    itens_pedido: List[ItemPedido] = []

    class Config:
        json_schema_extra = {
            'example': {
                'data_hora': 'datetime',
                'status': 'str',
                'frete': 'float',
                'loja_uuid': 'str',
                'endereco_uuid': 'str'
            }
        }
