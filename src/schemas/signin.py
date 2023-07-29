from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UsuarioSignIn(BaseModel):    
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    endereco_uuid: str
    password: str
    endereco_uuid: str



class LojaSignIn(BaseModel):    
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    password: str
