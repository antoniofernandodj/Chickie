from sqlalchemy import Column as Col, String, ForeignKey, Float
from src.infra.database.entities import Base


class ZonaEntrega(Base):
    __tablename__ = "zonas_de_entrga"

    uuid = Col(String(36), primary_key=True)
    nome = Col(String(255))
    cidade = Col(String(255))
    uf = Col(String(255))
    cep = Col(String(10))
    taxa_de_entrega = Col(Float)
    loja_uuid = Col(String(36), ForeignKey("lojas.uuid"))
