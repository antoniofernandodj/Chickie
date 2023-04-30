from flask_login import UserMixin
from src.infra.database.entities import BaseEntityClass
from src.infra.database.entities import Base
from typing import Optional
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import (
    Integer as Int, String as Str, Text
)


class User(Base, BaseEntityClass, UserMixin):
    
    __tablename__ = 'user'
    
    uuid = Col(Str(40), primary_key=True)
    name = Col(Str(50))
    email = Col(Str(50))
    password_hash = Col(Text)
