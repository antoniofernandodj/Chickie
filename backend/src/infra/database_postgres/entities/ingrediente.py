from src.infra.database_postgres.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import String as Str, Text


class Ingrediente(Base):   # database
    __tablename__ = "ingredientes"

    uuid = Col(Str(36), primary_key=True, unique=True, nullable=False)
    nome = Col(Text, nullable=False)
    descricao = Col(Text)
    produto_uuid = Col(Str(36), FK("produtos.uuid"), nullable=False)
    loja_uuid = Col(Str(36), FK("lojas.uuid"), nullable=False)
