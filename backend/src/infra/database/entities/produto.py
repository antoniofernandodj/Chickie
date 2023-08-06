from src.infra.database.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import String as Str, Text, Integer


class Produto(Base):
    __tablename__ = "produtos"

    uuid = Col(Str(36), primary_key=True)
    nome = Col(Str(100))
    descricao = Col(Text)
    categoria_uuid = Col(Str(36), FK("categorias_de_produtos.uuid"))
    loja_uuid = Col(Str(36), FK("lojas.uuid"))


class AvaliacaoDeProduto(Base):
    __tablename__ = "avaliacoes_de_produtos"

    uuid = Col(Str(36), primary_key=True)
    descricao = Col(Text)
    nota = Col(Integer)
    usuario_uuid = Col(Str(36), FK("usuarios.uuid"))
    produto_uuid = Col(Str(36), FK("produtos.uuid"))
