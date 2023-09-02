from src.infra.database.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from datetime import datetime
from sqlalchemy.types import Float, String as Str, DateTime


class Pedido(Base):
    __tablename__ = "pedidos"

    uuid = Col(Str(36), primary_key=True, unique=True)
    data_hora = Col(DateTime, default=datetime.utcnow)
    status_uuid = Col(Str(36), FK("status.uuid"), nullable=False)
    frete = Col(Float, nullable=False)
    loja_uuid = Col(Str(36), FK("lojas.uuid"), nullable=False)
    endereco_uuid = Col(Str(36), FK("enderecos.uuid"), nullable=False)
    usuario_uuid = Col(Str(36), FK("usuarios.uuid"), nullable=False)

    @property
    def total(self):
        from src.infra.database import session
        from src.infra.database import entities as e

        db = session.get()
        items = db.query(e.ItemPedido).filter_by(pedido_uuid=self.uuid).all()

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
