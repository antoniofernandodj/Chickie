from src.infra.database_postgres.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import String as Str, Text, Integer, Float


class Produto(Base):
    __tablename__ = "produtos"

    uuid = Col(Str(36), primary_key=True, unique=True)
    nome = Col(Text, nullable=False)
    descricao = Col(Text)
    preco = Col(Float)
    categoria_uuid = Col(
        Str(36), FK("categorias_de_produtos.uuid"), nullable=False
    )
    loja_uuid = Col(Str(36), FK("lojas.uuid"), nullable=False)


class AvaliacaoDeProduto(Base):
    __tablename__ = "avaliacoes_de_produtos"

    uuid = Col(Str(36), primary_key=True)
    descricao = Col(Text)
    nota = Col(Integer)
    usuario_uuid = Col(Str(36), FK("usuarios.uuid"), nullable=False)
    produto_uuid = Col(Str(36), FK("produtos.uuid"), nullable=False)
