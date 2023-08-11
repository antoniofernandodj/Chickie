from pydantic import BaseModel
from typing import Optional


class Status(BaseModel):
    __tablename__ = "status"

    nome: str
    descricao: str
    loja_uuid: str
    uuid: Optional[str] = None
