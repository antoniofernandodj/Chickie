from pydantic import BaseModel
from typing import Optional, List
from src.models import Preco


class Produto(BaseModel):
    __tablename__ = "produtos"
    nome: str
    descricao: str
    preco: float
    categoria_uuid: str
    loja_uuid: str

    uuid: Optional[str] = None


class ProdutoPOST(BaseModel):
    __tablename__ = "produtos"
    nome: str
    descricao: str
    preco: float
    categoria_uuid: str
    loja_uuid: str
    image_bytes: str
    filename: str

    uuid: Optional[str] = None


class ProdutoGET(BaseModel):
    __tablename__ = "produtos"
    nome: str
    descricao: str
    preco: float
    categoria_uuid: str
    loja_uuid: str
    precos: List[Preco]

    image_url: Optional[str] = None
    preco_hoje: Optional[float] = None
    uuid: Optional[str] = None
