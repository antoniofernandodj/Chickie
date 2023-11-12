from pydantic import BaseModel
from typing import Optional


class UsuarioSignIn(BaseModel):
    nome: str
    username: str
    email: str
    celular: str
    endereco_uuid: str
    password: str
    telefone: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'nome': 'User',
                    'username': 'user',
                    'email': 'user@email.com',
                    'telefone': '2127856985',
                    'celular': '21965896325',
                    'endereco_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565',
                    'password': 'minha_senha',
                },
                {
                    'nome': 'User',
                    'username': 'user',
                    'email': 'user@email.com',
                    'celular': '21963258741',
                    'endereco_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565',
                    'password': 'minha_senha',
                }
            ]
        }
    }



class LojaSignIn(BaseModel):
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    password: str
