from sqlalchemy import Column as Col, String, ForeignKey
from src.infra.database_postgres.entities import Base
from sqlalchemy.types import Text


class Status(Base):
    __tablename__ = "status"

    uuid = Col(String(36), primary_key=True, unique=True)
    nome = Col(Text, nullable=False)
    descricao = Col(Text)
    loja_uuid = Col(String(36), ForeignKey("lojas.uuid"), nullable=False)
