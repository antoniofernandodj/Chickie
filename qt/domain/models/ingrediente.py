from pydantic import BaseModel
from typing import Optional


class Ingrediente(BaseModel):
    __tablename__ = "ingredientes"

    nome: str
    descricao: str
    produto_uuid: str
    loja_uuid: str
    uuid: Optional[str] = None
