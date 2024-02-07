from pydantic import BaseModel  # type: ignore
from typing import Optional, List
from src.domain.data_models import EnderecoLoja


class LojaGET(BaseModel):
    __tablename__ = "lojas"
    nome: str
    username: str
    email: str
    celular: str
    uuid: str
    endereco: EnderecoLoja
    telefone: Optional[str] = None
    imagem_cadastro: Optional[str] = None
    horarios_de_funcionamento: Optional[str] = None


class Lojas(BaseModel):
    __tablename__ = "lojas"
    limit: int
    offset: int
    payload: List[LojaGET]
    length: int


class Loja(BaseModel):
    __tablename__ = "lojas"
    nome: str
    username: str
    email: str
    celular: str
    password_hash: str

    telefone: Optional[str] = None
    password: Optional[str] = None
    uuid: Optional[str] = None
    ativo: Optional[bool] = True
    passou_pelo_primeiro_acesso: Optional[bool] = False
    horarios_de_funcionamento: Optional[str] = None


class LojaPUT(BaseModel):

    email: str
    telefone: str
    celular: str

    nome: str
    username: str

    uf: str
    cep: str
    cidade: str
    logradouro: str
    bairro: str
    numero: str
    complemento: str

    horarios_de_funcionamento: Optional[str] = None
