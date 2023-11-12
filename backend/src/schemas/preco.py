from pydantic import BaseModel
from typing import Optional


class Preco(BaseModel):
    __tablename__ = "precos"
    produto_uuid: str
    valor: float
    dia_da_semana: str
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'produto_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565',
                'valor': 45.5,
                'dia_da_semana': 'seg'
            }
        }
    }
