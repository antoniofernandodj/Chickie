from src.infra.database.entities import BaseEntityClass
from src.infra.database.entities import Base, Loja
from typing import Optional
from sqlalchemy.orm import relationship as rel
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from datetime import datetime
from sqlalchemy.types import (
    Integer as Int, Float, String as Str, Text, Enum, DateTime
)
import enum

class StatusPedido(enum.Enum):
    Pendente = 'Pendente'
    Pago = 'Pago'
    EmEnvio = 'EmEnvio'
    Entregue = 'Entregue'
    Cancelado = 'Cancelado'


class Pedido(Base, BaseEntityClass):
    __tablename__ = 'pedidos'

    uuid = Col(Str(36), primary_key=True)
    data_hora = Col(DateTime, default=datetime.utcnow)
    status = Col(Enum(StatusPedido))
    frete = Col(Float)
    loja_uuid = Col(Str(36), FK('lojas.uuid'))
    endereco_uuid = Col(Str(36), FK('enderecos.uuid'))
    timestamp = Col(Float)

    @property
    def total(self):
        from src.infra.database import session
        from src.infra.database import entities as e
        from sqlalchemy.sql import func

        db = session.get()
        items = db.query(e.ItemPedido) \
            .filter_by(pedido_uuid=self.uuid) \
            .all()
        
        total = sum([float(item.subtotal) for item in items])
        return total

    # @property
    # def total(self):
    #     from src.infra.database import session
    #     from src.infra.database import entities as e
    #     from sqlalchemy.sql import func

    #     db = session.get()
    #     total = db.query(func.sum(e.ItemPedido.subtotal)) \
    #         .filter_by(pedido_uuid=self.uuid) \
    #         .scalar() or 0.0
        
    #     return total

