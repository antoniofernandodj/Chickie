from pydantic import BaseModel
from typing import Optional


class Entregador(BaseModel):
    __tablename__ = "entregadores"
    nome: str
    celular: str
    veiculo: str
    placa_veiculo: str
    loja_uuid: str
    
    telefone: Optional[str] = None
    email: Optional[str] = None
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'nome': 'Fulano de tal',
                'telefone': '2127263545',
                'celular': '21589652365',
                'veiculo': 'Fazer Preta',
                'placa_veiculo': 'XXX-XXX',
                'loja_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b'
            }
        }
    }
