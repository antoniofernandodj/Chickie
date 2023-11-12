from pydantic import BaseModel
from typing import Optional


class Feedback(BaseModel):
    __tablename__ = "feedbacks"
    usuario_uuid: str
    loja_uuid: str
    nota: float
    comentario: str
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'usuario_uuid': 'str',
                'loja_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b',
                'nota': 'float',
                'comentario': 'str'
            }
        }
    }
