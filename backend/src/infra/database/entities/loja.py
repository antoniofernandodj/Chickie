from src.infra.database.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey
from sqlalchemy.types import String as Str, Text


class Loja(Base):
    __tablename__ = "lojas"
    uuid = Col(Str(36), unique=True, primary_key=True)
    nome = Col(Text, nullable=False)
    username = Col(Text, unique=True)
    email = Col(Text, unique=True)
    telefone = Col(Text)
    celular = Col(Text)
    password_hash = Col(Text, nullable=False)
    endereco_uuid = Col(Str(36), ForeignKey("enderecos.uuid"), nullable=False)
