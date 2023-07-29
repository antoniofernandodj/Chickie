from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Usuario(BaseModel):
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    endereco_uuid: str
    password: Optional[str] = None
    password_hash: Optional[str] = None
    endereco_uuid: Optional[str] = None
    uuid: Optional[str] = None
