from src.infra.database_postgres.entities import Base
from sqlalchemy.schema import Column as Col
from sqlalchemy.types import String as Str, Text, Boolean


class Loja(Base):
    __tablename__ = "lojas"
    uuid = Col(Str(36), unique=True, primary_key=True, nullable=False)
    nome = Col(Text, nullable=False)
    username = Col(Text, unique=True)
    email = Col(Text, unique=True)
    telefone = Col(Text)
    celular = Col(Text, unique=True)
    password_hash = Col(Text, nullable=False)
    ativo = Col(Boolean, default=True)
    horarios_de_funcionamento = Col(Text)
    passou_pelo_primeiro_acesso = Col(Boolean, default=False)
