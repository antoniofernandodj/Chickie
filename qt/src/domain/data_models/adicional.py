from pydantic import BaseModel
from typing import Optional


class Adicional(BaseModel):
    __tablename__ = "status"

    nome: str
    loja_uuid: str
    descricao: str
    preco: float

    uuid: Optional[str] = None
