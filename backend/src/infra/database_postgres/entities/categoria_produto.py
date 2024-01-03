from src.infra.database_postgres.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import String as Str, Text


class CategoriaProduto(Base):
    __tablename__ = "categorias_de_produtos"
    uuid = Col(Str(36), unique=True, primary_key=True, nullable=False)
    nome = Col(Text, nullable=False)
    descricao = Col(Text)
    loja_uuid = Col(Text, FK("lojas.uuid"), nullable=False)
