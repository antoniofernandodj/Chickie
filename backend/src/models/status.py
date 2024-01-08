from pydantic import BaseModel
from typing import Optional


class Status(BaseModel):
    __tablename__ = "status"

    nome: str
    loja_uuid: str

    descricao: Optional[str] = None
    uuid: Optional[str] = None
