from pydantic import BaseModel
from typing import Optional


class AvaliacaoDeLoja(BaseModel):

    __tablename__ = "avaliacoes_de_loja"

    usuario_uuid: str
    loja_uuid: str
    nota: int
    descricao: str
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'usuario_uuid': 'str',
                'loja_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b',
                'nota': 'float',
                'descricao': 'str'
            }
        }
    }


class AvaliacaoDeProduto(BaseModel):

    __tablename__ = "avaliacoes_de_produtos"

    usuario_uuid: str
    loja_uuid: str
    produto_uuid: str
    nota: int
    descricao: str
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'usuario_uuid': 'str',
                'loja_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b',
                'nota': 'float',
                'descricao': 'str'
            }
        }
    }
