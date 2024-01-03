import enum
from src.infra.database_postgres.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import Float, String as Str, Enum


class DiasDaSemana(enum.Enum):
    seg = enum.auto()
    ter = enum.auto()
    qua = enum.auto()
    qui = enum.auto()
    sex = enum.auto()
    sab = enum.auto()
    dom = enum.auto()


class Preco(Base):
    __tablename__ = "precos"

    uuid = Col(Str(36), primary_key=True, unique=True, nullable=False)
    produto_uuid = Col(Str(36), FK("produtos.uuid"), nullable=False)
    valor = Col(Float)
    dia_da_semana = Col(Enum(DiasDaSemana))  # type: ignore
