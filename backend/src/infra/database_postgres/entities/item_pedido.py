from src.infra.database_postgres.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import Integer as Int, String as Str


class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    uuid = Col(Str(36), unique=True, primary_key=True, nullable=False)
    quantidade = Col(Int)
    produto_uuid = Col(Str(36), FK("produtos.uuid"))
    pedido_uuid = Col(Str(36), FK("pedidos.uuid", ondelete="CASCADE"))
    loja_uuid = Col(Str(36), FK("lojas.uuid"))
