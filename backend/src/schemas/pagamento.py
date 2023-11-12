from pydantic import BaseModel
from typing import Optional


class Pagamento(BaseModel):
    __tablename__ = "pagamentos"
    pedido_uuid: str
    metodo_pagamento_uuid: str
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'pedido_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b',
                'metodo_pagamento': '7613fa2f-8cde-4c66-bbb3-511a63546c9b'
            }
        }
    }
