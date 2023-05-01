from src.infra.database.entities import BaseEntityClass
from src.infra.database.entities import Base
from src.infra.database.entities import Produto, Pedido, Loja
from sqlalchemy.orm import relationship as rel
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import (
    Integer as Int, Float, String as Str, Text, Enum
)

class ItemPedido(Base, BaseEntityClass):
    __tablename__ = 'itens_pedido'

    uuid = Col(Str(40), primary_key=True)
    quantidade = Col(Int)
    subtotal = Col(Float)

    produto_uuid = Col(Str(40), FK('produtos.uuid'))
    produto = rel(Produto)

    pedido_uuid = Col(Str(40), FK('pedidos.uuid'))
    pedido = rel(Pedido, back_populates='items')

    loja_uuid = Col(Str(40), FK('lojas.uuid'))
    loja = rel(Loja, back_populates='produtos')