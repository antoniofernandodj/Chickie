from pydantic import BaseModel
from typing import Optional, List
from .ingrediente_item_pedido import IngredienteDeItemDePedido


class IngredientesSelect(BaseModel):
    uuid: str
    value: bool
    nome: Optional[str] = None


class ItemPedido(BaseModel):
    __tablename__ = "itens_pedido"
    quantidade: int
    observacoes: str
    pedido_uuid: str
    loja_uuid: str
    produto_nome: str
    produto_descricao: str
    valor: float
    uuid: Optional[str] = None


class ItemPedidoGET(BaseModel):
    __tablename__ = "itens_pedido"
    produto_nome: str
    produto_descricao: str
    quantidade: int
    observacoes: str
    pedido_uuid: str
    loja_uuid: str
    ingredientes: List[IngredienteDeItemDePedido]
    valor: float
    uuid: Optional[str] = None


class ItemPedidoPOST(BaseModel):
    quantidade: int
    observacoes: str
    produto_uuid: str
    ingredientes: List[IngredientesSelect]
    pedido_uuid: Optional[str] = None
    loja_uuid: Optional[str] = None
    valor: Optional[float] = 0
