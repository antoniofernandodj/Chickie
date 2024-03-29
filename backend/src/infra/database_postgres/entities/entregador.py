from sqlalchemy import Column as Col, String, ForeignKey
from src.infra.database_postgres.entities import Base
from sqlalchemy.types import Text


class Entregador(Base):
    __tablename__ = "entregadores"
    uuid = Col(String(36), unique=True, primary_key=True, nullable=False)
    nome = Col(Text, unique=True, nullable=False)
    telefone = Col(Text)
    email = Col(Text)
    celular = Col(Text)
    veiculo = Col(Text)
    placa_veiculo = Col(Text)
    loja_uuid = Col(Text, ForeignKey("lojas.uuid"), nullable=False)
