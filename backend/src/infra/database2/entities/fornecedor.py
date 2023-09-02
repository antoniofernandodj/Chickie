from sqlalchemy import Column as Col, String, ForeignKey
from sqlalchemy.types import Float, Text
from src.infra.database.entities import Base


class Fornecedor(Base):
    __tablename__ = "fornecedores"
    uuid = Col(String(36), unique=True, primary_key=True)
    nome = Col(Text, nullable=False)
    username = Col(Text, nullable=False, unique=True)
    email = Col(Text, nullable=False, unique=True)
    password_hash = Col(Text, nullable=False)
    celular = Col(Text)
    telefone = Col(Text)

    cnpj = Col(Text, unique=True, nullable=False)
    nota_avaliacao = Col(Float)
    loja_uuid = Col(String(36), ForeignKey("lojas.uuid"), nullable=False)
