from pydantic import BaseModel
from typing import Optional


class ItemPedido(BaseModel):
    __tablename__ = "itens_pedido"
    quantidade: int
    produto_uuid: str

    pedido_uuid: Optional[str] = None
    loja_uuid: Optional[str] = None
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'quantidade': 1,
                'produto_uuid': 'bff4a009-3e59-48ba-b8f3-ec0cc23a83dd',
            }
        }
    }
