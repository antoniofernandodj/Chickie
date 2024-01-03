from pydantic import BaseModel
from typing import Optional, List
from src.schemas import Preco


class Produto(BaseModel):
    __tablename__ = "produtos"
    nome: str
    descricao: str
    preco: float
    categoria_uuid: str
    loja_uuid: str

    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'nome': 'American Grill',
                'descricao': (
                    'Sanduíche tal com molho tal,'
                    'pão tal e carne tal'
                ),
                'preco': 30.35,
                'categoria_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565',
                'loja_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b'
            }
        }
    }


class ProdutoGET(BaseModel):
    __tablename__ = "produtos"
    nome: str
    descricao: str
    preco: float
    categoria_uuid: str
    loja_uuid: str
    precos: List[Preco]

    uuid: Optional[str] = None
