import enum
from flask_login import UserMixin
from src.infra.database.entities import BaseEntityClass
from src.infra.database.entities import Base
from .endereco import Endereco
from sqlalchemy.orm import relationship as rel
from typing import Optional
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import (
    Integer as Int, String as Str, Text, Enum
)

class Grupo(enum.Enum):
    ADMIN = enum.auto()
    SUPERVISOR = enum.auto()
    CLIENTE = enum.auto()


class Usuario(Base, BaseEntityClass, UserMixin):
    
    __tablename__ = 'usuarios'
    
    uuid = Col(Str(40), primary_key=True)
    nome = Col(Str(50))
    username = Col(Str(50))
    email = Col(Str(50))
    telefone = Col(Str(50))
    celular = Col(Str(50))
    password_hash = Col(Text)

    endereco_uuid = Col(Str(40), FK('enderecos.uuid'))
    endereco = rel(Endereco, uselist=False, back_populates='usuario')
