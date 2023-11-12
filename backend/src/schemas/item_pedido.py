from pydantic import BaseModel
from typing import Optional


class ItemPedido(BaseModel):
    __tablename__ = "itens_pedido"
    quantidade: int
    produto_uuid: str
    pedido_uuid: str
    loja_uuid: str
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'quantidade': 'int',
                'produto_uuid': 'str',
                'pedido_uuid': 'str',
                'loja_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b'
            }
        }
    }
