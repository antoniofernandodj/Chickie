from pydantic import BaseModel
from typing import Optional


class Pagamento(BaseModel):
    __tablename__ = "pagamentos"
    pedido_uuid: str
    metodo_pagamento: str
    uuid: Optional[str] = None

    class Config:
        json_schema_extra = {
            'example': {
                'pedido_uuid': 'str',
                'metodo_pagamento': 'str'
            }
        }
