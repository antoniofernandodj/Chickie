from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Produto(BaseModel):
    nome: str
    descricao: str
    categoria_de_produto_uuid: str
    loja_uuid: str
    uuid: Optional[str] = None

