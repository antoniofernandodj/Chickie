from sqlalchemy import Column as Col, String, Text, Float, ForeignKey
from src.infra.database.entities import Base


class Feedback(Base):
    __tablename__ = "feedbacks"

    usuario_uuid = Col(String(36), ForeignKey("usuarios.uuid"))
    loja_uuid = Col(String(36), ForeignKey("lojas.uuid"))
    nota = Col(Float, nullable=False)
    comentario = Col(Text)
