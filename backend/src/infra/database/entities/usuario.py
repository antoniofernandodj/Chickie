from src.infra.database.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import String as Str, Text


class Usuario(Base):
    __tablename__ = "usuarios"

    uuid = Col(Str(36), primary_key=True)
    nome = Col(Str(100))
    username = Col(Str(100))
    email = Col(Str(100))
    telefone = Col(Str(20))
    celular = Col(Str(20))
    password_hash = Col(Text)

    endereco_uuid = Col(Str(40), FK("enderecos.uuid"))
