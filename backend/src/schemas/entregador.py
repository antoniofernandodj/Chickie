from pydantic import BaseModel
from typing import Optional


class Entregador(BaseModel):
    __tablename__ = "entregadores"
    nome: str
    telefone: str
    celular: str
    veiculo: str
    placa_veiculo: str
    loja_uuid: str
    uuid: Optional[str] = None

    class Config:
        json_schema_extra = {
            'example': {
                'nome': 'str',
                'telefone': 'str',
                'celular': 'str',
                'veiculo': 'str',
                'placa_veiculo': 'str',
                'loja_uuid': 'str'
            }
        }
