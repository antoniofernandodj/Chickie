from sqlalchemy import (
    Column as Col, Integer, String, Float, ForeignKey
)
from sqlalchemy.orm import relationship
from src.infra.database.entities import Base


class Entregador(Base):
    __tablename__ = 'entregadores'

    id = Col(Integer, primary_key=True)
    nome = Col(String(100), nullable=False)
    telefone = Col(String(20))
    celular = Col(String(20))
    veiculo = Col(String(50))
    placa_veiculo = Col(String(10))
    loja_uuid = Col(String(36), ForeignKey('lojas.uuid'))
    timestamp = Col(Float)
