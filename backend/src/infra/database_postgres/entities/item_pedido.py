from src.infra.database_postgres.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import Integer as Int, String as Str, Text, Float


class ItemPedido(Base):  # database
    __tablename__ = "itens_pedido"
    uuid = Col(Str(36), unique=True, primary_key=True, nullable=False)
    produto_nome = Col(Text)
    produto_descricao = Col(Text)
    quantidade = Col(Int)
    observacoes = Col(Text)
    pedido_uuid = Col(Str(36), FK("pedidos.uuid", ondelete="CASCADE"))
    loja_uuid = Col(Str(36), FK("lojas.uuid"))
    valor = Col(Float)
