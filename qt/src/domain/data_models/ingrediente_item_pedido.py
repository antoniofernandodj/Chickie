from pydantic import BaseModel
from typing import Optional


class IngredienteDeItemDePedido(BaseModel):
    __tablename__ = "ingredientes_item_pedido"

    nome: str
    descricao: str
    loja_uuid: str
    item_uuid: str
    incluso: bool
    uuid: Optional[str] = None
