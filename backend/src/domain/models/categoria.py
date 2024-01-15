from pydantic import BaseModel
from typing import Optional


class CategoriaProdutos(BaseModel):
    __tablename__ = "categorias_de_produtos"
    nome: str
    descricao: str
    loja_uuid: str

    uuid: Optional[str] = None
