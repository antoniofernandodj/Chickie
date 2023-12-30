from pydantic import BaseModel
from typing import Optional, List, Annotated
from .item_pedido import ItemPedido


isodatetime = Annotated[str, 'isotime']


class Pedido(BaseModel):
    __tablename__ = "pedidos"
    data_hora: isodatetime
    status_uuid: str
    loja_uuid: str
    endereco_uuid: str

    frete: float
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'data_hora': '2023-11-11T14:30:00.000Z',
                    'status_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565',
                    'frete': 45.12,
                    'loja_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b',
                    'endereco_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565'
                }
            ]
        }
    }


class PedidoItens(BaseModel):
    __tablename__ = "pedidos"
    data_hora: isodatetime
    status_uuid: str
    frete: float
    loja_uuid: str
    endereco_uuid: str
    uuid: Optional[str] = None
    itens_pedido: List[ItemPedido] = []

    class Config:
        json_schema_extra = {
            'example': {
                'data_hora': '2023-11-11T14:30:00.000Z',
                'status_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565',
                'frete': 12.75,
                'loja_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b',
                'endereco_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565'
            }
        }
