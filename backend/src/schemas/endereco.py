from pydantic import BaseModel
from typing import Optional


class Endereco(BaseModel):
    __tablename__ = "enderecos"
    uf: str
    cidade: str
    logradouro: str
    numero: str
    bairro: str
    cep: str
    complemento: str = ""
    uuid: Optional[str] = None
