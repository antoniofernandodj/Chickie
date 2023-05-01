import enum
from src.infra.database.entities import BaseEntityClass
from src.infra.database.entities import Base
from typing import Optional
from sqlalchemy.orm import relationship as rel
from src.infra.database.entities import Categoria, Loja
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import (
    Integer as Int, Float, String as Str, Text, Enum
)

class Produto(Base, BaseEntityClass):

    __tablename__ = 'produtos'


    uuid = Col(Str(40), primary_key=True)
    nome = Col(Str(70))
    descricao = Col(Text)

    categoria_uuid = Col(Str(40), FK('categorias.uuid'))
    categoria = rel(Categoria, back_populates='produtos')

    loja_uuid = Col(Str(40), FK('lojas.uuid'))
    loja = rel(Loja, back_populates='produtos')

    imagem_url = Col(Text)
