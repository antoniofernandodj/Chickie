from sqlalchemy import Column as Col, String, ForeignKey
from src.infra.database.entities import Base
from sqlalchemy.types import Text


class Entregador(Base):
    __tablename__ = "entregadores"
    uuid = Col(String(36), unique=True, primary_key=True)
    nome = Col(Text, nullable=False)
    telefone = Col(Text)
    celular = Col(Text)
    veiculo = Col(Text)
    placa_veiculo = Col(Text)
    loja_uuid = Col(Text, ForeignKey("lojas.uuid"))
