from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CategoriaProdutos(BaseModel):
    nome: str
    descricao: str
    loja_uuid: str
    uuid: Optional[str] = None
