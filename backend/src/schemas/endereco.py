from pydantic import BaseModel
from typing import Optional


class Endereco(BaseModel):
    __tablename__ = "enderecos"
    uf: str
    cidade: str
    logradouro: str
    numero: str
    bairro: str

    cep: Optional[str] = None
    complemento: Optional[str] = None
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'uf': 'RJ',
                'cidade': 'Rio de Janeiro',
                'logradouro': 'Rua Orestes de Souza',
                'numero': '245',
                'bairro': 'Vila Velha',
                'cep': '(Opcional) 24565444',
                'complemento': '(Optional) Casa 75'
            }
        }
    }


class EnderecoLoja(BaseModel):
    __tablename__ = "enderecos_lojas"
    uf: str
    cidade: str
    logradouro: str
    numero: str
    bairro: str
    loja_uuid: str

    cep: Optional[str] = None
    complemento: Optional[str] = None
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'uf': 'RJ',
                'cidade': 'Rio de Janeiro',
                'logradouro': 'Rua Orestes de Souza',
                'numero': '245',
                'bairro': 'Vila Velha',
                'cep': '(Opcional) 24565444',
                'complemento': '(Optional) Casa 75',
                'loja_uuid': '...'
            }
        }
    }


class EnderecoUsuario(BaseModel):
    __tablename__ = "enderecos_usuarios"
    uf: str
    cidade: str
    logradouro: str
    numero: str
    bairro: str
    usuario_uuid: str

    cep: Optional[str] = None
    complemento: Optional[str] = None
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'uf': 'RJ',
                'cidade': 'Rio de Janeiro',
                'logradouro': 'Rua Orestes de Souza',
                'numero': '245',
                'bairro': 'Vila Velha',
                'cep': '(Opcional) 24565444',
                'complemento': '(Optional) Casa 75',
                'usuario_uuid': '...'
            }
        }
    }


class EnderecoEntrega(BaseModel):
    __tablename__ = "enderecos_entregas"
    uf: str
    cidade: str
    logradouro: str
    numero: str
    bairro: str
    pedido_uuid: str

    cep: Optional[str] = None
    complemento: Optional[str] = None
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'uf': 'RJ',
                'cidade': 'Rio de Janeiro',
                'logradouro': 'Rua Orestes de Souza',
                'numero': '245',
                'bairro': 'Vila Velha',
                'cep': '(Opcional) 24565444',
                'complemento': '(Optional) Casa 75',
                'pedido_uuid': '...'
            }
        }
    }
