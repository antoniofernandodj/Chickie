from sqlalchemy import (
    Column as Col, Integer, String,
    Date, ForeignKey, Float, Text
)
from src.infra.database.entities import Base


class Pagamento(Base):
    __tablename__ = 'pagamentos'

    uuid = Col(String(36), primary_key=True)
    pedido_uuid = Col(String(36), ForeignKey('pedidos.uuid'))
    metodo_pagamento = Col(String(100))
    timestamp = Col(Float)


class MetodosPagamento(Base):
    __tablename__ = 'metodos_pagamento'
    uuid = Col(String(36), primary_key=True)
    loja_uuid = Col(String(36), ForeignKey('lojas.uuid'))
    nome = Col(String(100))
    Descricao = Col(Text)
