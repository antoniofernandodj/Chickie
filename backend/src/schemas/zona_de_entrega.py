from pydantic import BaseModel
from typing import Optional


class ZonaDeEntrega(BaseModel):
    __tablename__ = "zonas_de_entrega"

    nome: str
    cidade: str
    uf: str
    bairro: str
    cep: str
    taxa_de_entrega: float
    loja_uuid: str
    uuid: Optional[str] = None
