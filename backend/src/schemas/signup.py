from pydantic import BaseModel
from typing import Optional


class UsuarioSignUp(BaseModel):

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

    modo_de_cadastro: str

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


class LojaSignUp(BaseModel):
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    password: str

    uf: str
    cep: str
    cidade: str
    logradouro: str
    bairro: str
    numero: str
    complemento: str

    horarios_de_funcionamento: Optional[str] = None
    image_filename: str | None = None
    image_bytes: str | None = None

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'nome': 'Store',
                    'username': 'store',
                    'email': 'store@email.com',
                    'telefone': '2127856985',
                    'celular': '21965896325',
                    'password': 'store_password',

                    'uf': 'UF',
                    'cep': '12345678',
                    'cidade': 'City',
                    'logradouro': 'Street',
                    'bairro': 'Neighborhood',
                    'numero': '123',
                    'complemento': 'Complement',

                    'horarios_de_funcionamento': 'Seg a Sáb, até 19h',
                    'image_filename': 'store_image.png',
                    'image_bytes': 'base64_encoded_string'
                },
                {
                    'nome': 'Another Store',
                    'username': 'another_store',
                    'email': 'another_store@email.com',
                    'telefone': '2127856985',
                    'celular': '21965896325',
                    'password': 'another_store_password',

                    'uf': 'UF',
                    'cep': '12345678',
                    'cidade': 'City',
                    'logradouro': 'Street',
                    'bairro': 'Neighborhood',
                    'numero': '456',
                    'complemento': 'Complement',

                    'horarios_de_funcionamento': 'Seg a Sáb, até 19h',
                    'image_filename': None,
                    'image_bytes': None
                }
            ]
        }
    }
    