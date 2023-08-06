from pydantic import BaseModel
from typing import Optional


class Produto(BaseModel):
    __tablename__ = "produtos"
    nome: str
    descricao: str
    categoria_uuid: str
    loja_uuid: str
    uuid: Optional[str] = None
