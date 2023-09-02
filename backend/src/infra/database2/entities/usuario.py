from src.infra.database.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import String as Str, Text


class Usuario(Base):
    __tablename__ = "usuarios"

    uuid = Col(Str(36), primary_key=True)
    nome = Col(Text, nullable=False)
    username = Col(Text, nullable=False, unique=True)
    email = Col(Text, nullable=False, unique=True)
    telefone = Col(Text)
    celular = Col(Text)
    password_hash = Col(Text, nullable=False)

    endereco_uuid = Col(Str(40), FK("enderecos.uuid"), nullable=False)
