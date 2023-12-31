from pydantic import BaseModel
from typing import Optional


class UsuarioSignIn(BaseModel):

    nome: str
    username: str
    email: str
    celular: str
    password: str

    bairro: str
    cep: str
    cidade: str
    complemento: str
    logradouro: str
    numero: str
    uf: str

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
                    'password': 'minha_senha',

                    'bairro': 'str',
                    'cep': 'str',
                    'cidade': 'str',
                    'complemento': 'str',
                    'logradouro': 'str',
                    'numero': 'str',
                    'uf': 'str'

                },
                {
                    'nome': 'User',
                    'username': 'user',
                    'email': 'user@email.com',
                    'celular': '21963258741',
                    'password': 'minha_senha',

                    'bairro': 'str',
                    'cep': 'str',
                    'cidade': 'str',
                    'complemento': 'str',
                    'logradouro': 'str',
                    'numero': 'str',
                    'uf': 'str'
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
