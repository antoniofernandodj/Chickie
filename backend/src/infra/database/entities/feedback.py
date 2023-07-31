from sqlalchemy import (
    Column as Col, Integer, String, Text, Float, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from src.infra.database.entities import Base


class Feedback(Base):
    __tablename__ = 'feedbacks'

    id = Col(String(36), primary_key=True)
    usuario_uuid = Col(String(36), ForeignKey('usuarios.uuid'))
    loja_uuid = Col(String(36), ForeignKey('lojas.uuid'))
    timestamp = Col(Float)
    nota = Col(Float, nullable=False)
    comentario = Col(Text)
