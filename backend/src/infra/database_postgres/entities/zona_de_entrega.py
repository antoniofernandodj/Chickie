from sqlalchemy import Column as Col, String, ForeignKey, Float
from src.infra.database_postgres.entities import Base
from sqlalchemy.types import Text


class ZonaEntrega(Base):
    __tablename__ = "zonas_de_entrega"

    uuid = Col(String(36), primary_key=True, unique=True)
    cidade = Col(Text)
    uf = Col(Text)
    bairro = Col(Text)
    cep = Col(Text)
    taxa_de_entrega = Col(Float)
    loja_uuid = Col(String(36), ForeignKey("lojas.uuid"), nullable=False)
