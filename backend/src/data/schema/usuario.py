from __future__ import annotations

from pydantic import BaseModel


class UsuarioDados(BaseModel):
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    password1: str
    password2: str
