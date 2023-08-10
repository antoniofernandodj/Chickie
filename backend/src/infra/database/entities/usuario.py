from src.infra.database.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import String as Str, Text


class Usuario(Base):
    __tablename__ = "usuarios"

    uuid = Col(Str(36), primary_key=True)
    nome = Col(Text)
    username = Col(Text)
    email = Col(Text)
    telefone = Col(Text)
    celular = Col(Text)
    password_hash = Col(Text)

    endereco_uuid = Col(Str(40), FK("enderecos.uuid"))
