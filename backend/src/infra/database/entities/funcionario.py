from sqlalchemy import (
    Column as Col, ForeignKey,
    String, Float
)
from src.infra.database.entities import Base


class Funcionario(Base):
    __tablename__ = 'funcionarios'

    uuid = Col(String(36), primary_key=True)
    loja_uuid = Col(String(36), ForeignKey('lojas.uuid'))
    cargo = Col(String(100))
    
    nome = Col(String(100))
    username = Col(String(100))
    email = Col(String(100))
    telefone = Col(String(20))
    celular = Col(String(100))
    password_hash = Col(String(100))
    timestamp = Col(Float)

    endereco_uuid = Col(
        String(36),
        ForeignKey('enderecos.uuid')
    )
