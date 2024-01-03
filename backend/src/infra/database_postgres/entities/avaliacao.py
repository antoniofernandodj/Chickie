from sqlalchemy import Column as Col, String, Text, ForeignKey, Integer
from src.infra.database_postgres.entities import Base


class AvaliacaoDeLoja(Base):

    __tablename__ = "avaliacoes_de_loja"

    uuid = Col(String(36), unique=True, primary_key=True, nullable=False)
    usuario_uuid = Col(String(36), ForeignKey("usuarios.uuid"), nullable=False)
    loja_uuid = Col(String(36), ForeignKey("lojas.uuid"), nullable=False)
    nota = Col(Integer, nullable=False)
    descricao = Col(Text)


class AvaliacaoDeProduto(Base):

    __tablename__ = "avaliacoes_de_produtos"

    uuid = Col(String(36), unique=True, primary_key=True, nullable=False)
    usuario_uuid = Col(String(36), ForeignKey("usuarios.uuid"), nullable=False)
    loja_uuid = Col(String(36), ForeignKey("lojas.uuid"), nullable=False)
    produto_uuid = Col(String(36), ForeignKey("produtos.uuid"), nullable=False)
    nota = Col(Integer, nullable=False)
    descricao = Col(Text)
