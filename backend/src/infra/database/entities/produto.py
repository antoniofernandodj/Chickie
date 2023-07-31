import enum
from src.infra.database.entities import BaseEntityClass
from src.infra.database.entities import Base
from typing import Optional
from sqlalchemy.orm import relationship as rel
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import (
    Integer as Int, Float, String as Str, Text, Enum
)

class Produto(Base, BaseEntityClass):

    __tablename__ = 'produtos'

    uuid = Col(Str(36), primary_key=True)
    nome = Col(Str(100))
    descricao = Col(Text)
    categoria_uuid = Col(
        Str(36), FK('categorias_de_produtos.uuid')
    )
    loja_uuid = Col(Str(36), FK('lojas.uuid'))
    timestamp = Col(Float)
