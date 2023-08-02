from src.infra.database.entities import BaseEntityClass
from src.infra.database.entities import Base
from sqlalchemy.orm import relationship as rel
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import (
    Float, String as Str, Text
)

class CategoriaProduto(Base, BaseEntityClass):
    __tablename__ = 'categorias_de_produtos'
    uuid = Col(Str(40), primary_key=True)
    nome = Col(Str(40))
    descricao = Col(Text)
    loja_uuid = Col(Str(40), FK('lojas.uuid'))
    timestamp = Col(Float)
