from pydantic import BaseModel
from typing import Optional


class ZonaDeEntrega(BaseModel):
    __tablename__ = "zonas_de_entrega"

    nome: str
    cidade: str
    uf: str
    
    taxa_de_entrega: float
    loja_uuid: str

    bairro: Optional[str] = None
    cep: Optional[str] = None
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'nome': 'Galo branco',
                'cidade': 'São Gonçalo',
                'uf': 'RJ',
                'bairro': 'Galo Branco (Opcional)',
                'cep': '24422400 (Opcional)',
                'taxa_de_entrega': 12.0,
                'loja_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565',
            }
        }
    }
