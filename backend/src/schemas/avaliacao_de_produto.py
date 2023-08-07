from pydantic import BaseModel
from typing import Optional


class AvaliacaoDeProduto(BaseModel):
    __tablename__ = "avaliacoes_de_produtos"
    descricao: str
    nota: int
    usuario_uuid: str
    produto_uuid: str
    uuid: Optional[str] = None
