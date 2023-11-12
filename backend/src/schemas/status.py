from pydantic import BaseModel
from typing import Optional


class Status(BaseModel):
    __tablename__ = "status"

    nome: str
    loja_uuid: str

    descricao: Optional[str] = None
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'nome': 'Em preparação',
                'descricao': '(Opcional) O sanduíche em questão está em preparação na cozinha',
                'loja_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565',
            }
        }
    }
