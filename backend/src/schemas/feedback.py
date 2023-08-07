from pydantic import BaseModel
from typing import Optional


class Feedback(BaseModel):
    __tablename__ = "feedbacks"
    usuario_uuid: str
    loja_uuid: str
    nota: float
    comentario: str
    uuid: Optional[str] = None
