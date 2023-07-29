from __future__ import annotations
from pydantic import BaseModel


class VincularClienteDados(BaseModel):
    loja_uuid: str
    usuario_uuid: str


class CadastrarLojaDados(BaseModel):
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    password1: str
    password2: str
