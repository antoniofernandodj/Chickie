from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Loja(BaseModel):
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    password_hash: str
    password: str
    grupo: str
        
    uuid: Optional[str] = None
