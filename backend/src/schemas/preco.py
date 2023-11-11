from pydantic import BaseModel
from typing import Optional


class Preco(BaseModel):
    __tablename__ = "precos"
    produto_uuid: str
    valor: float
    dia_da_semana: str
    uuid: Optional[str] = None

    class Config:
        json_schema_extra = {
            'example': {
                'produto_uuid': 'str',
                'valor': 'float',
                'dia_da_semana': 'str'
            }
        }
