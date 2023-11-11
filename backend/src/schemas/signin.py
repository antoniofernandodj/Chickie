from pydantic import BaseModel
from typing import Optional


class UsuarioSignIn(BaseModel):
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    endereco_uuid: str
    password: str
    loja_uuid: Optional[str] = None

    class Config:
        json_schema_extra = {
            'example': {
                'nome': 'str',
                'username': 'str',
                'email': 'str',
                'telefone': 'str',
                'celular': 'str',
                'endereco_uuid': 'str',
                'password': 'str',
                'loja_uuid': 'Optional[str]'
            }
        }



class LojaSignIn(BaseModel):
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    password: str
