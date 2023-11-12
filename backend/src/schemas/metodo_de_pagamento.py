from pydantic import BaseModel
from typing import Optional


class MetodoDePagamento(BaseModel):
    __tablename__ = "metodos_pagamento"
    loja_uuid: str
    nome: str
    descricao: Optional[str] = None
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'loja_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b',
                'nome': 'Cartão de crédito',
                'descricao': '(Opcional) Cartão de crédito'
            }
        }
    }
