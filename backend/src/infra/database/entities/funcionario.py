from sqlalchemy import Column as Col, ForeignKey, String
from src.infra.database.entities import Base


class Funcionario(Base):
    __tablename__ = "funcionarios"
    uuid = Col(String(36), unique=True, primary_key=True)
    nome = Col(String(100))
    loja_uuid = Col(String(36), ForeignKey("lojas.uuid"))
    cargo = Col(String(100))

    username = Col(String(100))
    email = Col(String(100))
    telefone = Col(String(20))
    celular = Col(String(100))
    password_hash = Col(String(100))
