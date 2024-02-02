from src.infra.database_postgres.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import String as Str, Text, Boolean


class IngredienteDeItemDePedido(Base):   # database
    __tablename__ = "ingredientes_item_pedido"

    uuid = Col(Str(36), primary_key=True, unique=True, nullable=False)
    nome = Col(Text, nullable=False)
    item_uuid = Col(Str(36), FK("itens_pedido.uuid"), nullable=False)
    descricao = Col(Text)
    incluso = Col(Boolean, nullable=False)
    loja_uuid = Col(Str(36), FK("lojas.uuid"), nullable=False)
