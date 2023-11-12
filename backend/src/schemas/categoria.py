from pydantic import BaseModel
from typing import Optional


class CategoriaProdutos(BaseModel):
    __tablename__ = "categorias_de_produtos"
    nome: str
    descricao: str
    loja_uuid: str

    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'nome': 'Bebidas',
                'descricao': 'Categoria destinada a catalogar as bebidas não alcoólicas da loja',
                'loja_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b'
            }
        }
    }
