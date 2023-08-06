from sqlalchemy import Column as Col, String, ForeignKey
from src.infra.database.entities import Base


class Entregador(Base):
    __tablename__ = "entregadores"

    nome = Col(String(100), nullable=False)
    telefone = Col(String(20))
    celular = Col(String(20))
    veiculo = Col(String(50))
    placa_veiculo = Col(String(10))
    loja_uuid = Col(String(36), ForeignKey("lojas.uuid"))
