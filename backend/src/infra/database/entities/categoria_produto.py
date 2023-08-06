from src.infra.database.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import String as Str, Text


class CategoriaProduto(Base):
    __tablename__ = "categorias_de_produtos"
    nome = Col(Str(40))
    descricao = Col(Text)
    loja_uuid = Col(Str(40), FK("lojas.uuid"))
