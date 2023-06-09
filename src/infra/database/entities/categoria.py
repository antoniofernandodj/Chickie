from src.infra.database.entities import BaseEntityClass
from src.infra.database.entities import Base, Loja
from sqlalchemy.orm import relationship as rel
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import (
    Integer as Int, Float, String as Str, Text, Enum
)

class Categoria(Base, BaseEntityClass):
    __tablename__ = 'categorias'

    uuid = Col(Str(40), primary_key=True)
    nome = Col(Str(40))

    descricao = Col(Text)

    loja_uuid = Col(Str(40), FK('lojas.uuid'))
    # loja = rel(Loja, back_populates='produtos')