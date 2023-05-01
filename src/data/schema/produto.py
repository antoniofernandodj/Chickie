from __future__ import annotations

from pydantic import BaseModel


class ProdutoDados(BaseModel):
    nome: str
    descricao: str
    categoria: str
    loja_uuid: str
