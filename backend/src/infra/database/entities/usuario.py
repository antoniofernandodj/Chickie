import enum
from src.lib.auth.classes import UserMixin
from src.infra.database.entities import BaseEntityClass
from src.infra.database.entities import Base
from typing import Optional
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import (
    Integer as Int, String as Str, Text, Enum, Float
)

class Usuario(Base, BaseEntityClass, UserMixin):
    
    __tablename__ = 'usuarios'
    
    uuid = Col(Str(36), primary_key=True)
    nome = Col(Str(100))
    username = Col(Str(100))
    email = Col(Str(100))
    telefone = Col(Str(20))
    celular = Col(Str(20))
    password_hash = Col(Text)
    timestamp = Col(Float)

    endereco_uuid = Col(Str(40), FK('enderecos.uuid'))
