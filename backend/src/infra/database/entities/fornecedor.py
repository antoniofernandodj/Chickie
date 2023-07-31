from sqlalchemy import Column as Col, String, ForeignKey
from sqlalchemy.types import Float
from src.infra.database.entities import Base


class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    uuid = Col(String(36), primary_key=True)

    nome = Col(String(100))
    username = Col(String(100))
    celular = Col(String(100))
    password_hash = Col(String(100))
    email = Col(String(100))
    telefone = Col(String(20))
    
    cnpj = Col(String(18), unique=True)
    site = Col(String(200))
    nota_avaliacao = Col(Float)
    loja_uuid = Col(String(36), ForeignKey('lojas.uuid'))
    timestamp = Col(Float)
