from pydantic import BaseModel
from typing import Optional


class Funcionario(BaseModel):
    __tablename__ = "funcionarios"
    loja_uuid: str
    cargo: str
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    pasword_hash: str
    uuid: Optional[str] = None
