from pydantic import BaseModel
from typing import Optional


class Feedback(BaseModel):
    __tablename__ = "feedbacks"
    usuario_uuid: str
    loja_uuid: str
    nota: float
    comentario: str
    uuid: Optional[str] = None

    class Config:
        json_schema_extra = {
            'example': {
                'usuario_uuid': 'str',
                'loja_uuid': 'str',
                'nota': 'float',
                'comentario': 'str'
            }
        }
