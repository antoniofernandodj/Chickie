from sqlalchemy import (
    Column as Col, Integer, String,
    Text, Float, ForeignKey, DateTime
)
from sqlalchemy.orm import relationship
from src.infra.database.entities import Base


class CupomDesconto(Base):
    __tablename__ = 'cupons_desconto'

    id = Col(Integer, primary_key=True)
    codigo = Col(String(20), unique=True, nullable=False)
    descricao = Col(Text)
    valor_desconto = Col(
        Float, nullable=False
    )
    data_validade = Col(
        DateTime, nullable=False
    )
    quantidade_disponivel = Col(
        Integer, nullable=False, default=1
    )
    quantidade_utilizada = Col(
        Integer, nullable=False, default=0
    )
    loja_uuid = Col(String(36), ForeignKey('lojas.uuid'))
    timestamp = Col(Float)
