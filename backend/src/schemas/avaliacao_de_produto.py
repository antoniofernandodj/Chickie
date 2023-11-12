from pydantic import BaseModel
from typing import Optional


class AvaliacaoDeProduto(BaseModel):
    __tablename__ = "avaliacoes_de_produtos"
    descricao: str
    nota: int
    usuario_uuid: str
    produto_uuid: str
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'descricao': 'Adorei o produto, qualidade excelente!',
                'nota': 3,
                'usuario_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565',
                'produto_uuid': '6187967d-c5d7-4640-af33-5a13a5c3g587'
            }
        }
    }
