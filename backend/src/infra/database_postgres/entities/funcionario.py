from sqlalchemy import Column as Col, ForeignKey, String
from src.infra.database_postgres.entities import Base
from sqlalchemy.types import Text


class Funcionario(Base):
    __tablename__ = "funcionarios"
    uuid = Col(String(36), unique=True, primary_key=True, nullable=False)
    nome = Col(Text, nullable=False)
    loja_uuid = Col(String(36), ForeignKey("lojas.uuid"), nullable=False)
    cargo = Col(Text)

    username = Col(Text, nullable=False, unique=True)
    email = Col(Text)
    telefone = Col(Text)
    celular = Col(Text)
    password_hash = Col(Text, nullable=False)
