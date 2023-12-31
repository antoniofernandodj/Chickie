from pydantic import BaseModel
from src.schemas import Endereco, Status
from typing import Optional, List, Annotated
from .item_pedido import ItemPedido
from datetime import datetime


isodatetime = Annotated[str, 'isotime']


class Pedido(BaseModel):
    __tablename__ = "pedidos"
    data_hora: isodatetime
    loja_uuid: str
    endereco_uuid: str
    frete: float
    celular: str

    status_uuid: Optional[str] = None
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'data_hora': '2023-11-11T14:30:00.000Z',
                    'frete': 45.12,
                    'loja_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b',
                    'endereco_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565'
                },
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
    data_hora: isodatetime | datetime
    frete: float
    loja_uuid: str
    celular: str
    uuid: Optional[str] = None
    status_uuid: Optional[str] = None
    status: Optional[Status] = None
    endereco_uuid: Optional[str] = None
    endereco: Optional[Endereco] = None
    itens_pedido: List[ItemPedido] = []

    class Config:
        json_schema_extra = {
            'example': {
                'data_hora': '2023-11-11T14:30:00.000Z',
                'status_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565',
                'frete': 12.75,
                'loja_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b',
                'endereco_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565',
                'itens_pedido': [
                    {
                        'quantidade': 2,
                        'produto_uuid': 'bff4a009-3e59-48ba-b8f3-ec0cc23a83dd',
                    },
                    {
                        'quantidade': 1,
                        'produto_uuid': 'f16d8b35-1a0b-4215-a7da-f5ae9748ffc0',
                    }
                ]
            }
        }
