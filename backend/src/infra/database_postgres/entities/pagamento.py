from sqlalchemy import Column as Col, String, ForeignKey, Text
from src.infra.database_postgres.entities import Base


class Pagamento(Base):
    __tablename__ = "pagamentos"

    uuid = Col(String(36), primary_key=True, unique=True)
    pedido_uuid = Col(String(36), ForeignKey("pedidos.uuid"), nullable=False)
    metodo_pagamento_uuid = Col(
        String(36), ForeignKey("metodos_pagamento.uuid"), nullable=False
    )


class MetodosPagamento(Base):
    __tablename__ = "metodos_pagamento"
    uuid = Col(String(36), primary_key=True)
    loja_uuid = Col(String(36), ForeignKey("lojas.uuid"), nullable=False)
    nome = Col(Text, nullable=False, unique=True)
    Descricao = Col(Text)
