from sqlalchemy.orm import relationship
from sqlalchemy import (
    String,
    ForeignKey,
    Column as Col,
)
from sqlalchemy.types import Float
from src.infra.database_postgres.entities import Base


class ProgramaFidelidade(Base):
    __tablename__ = "programa_fidelidade"
    uuid = Col(String(36), unique=True, primary_key=True, nullable=False)
    nome = Col(String(100), nullable=False)
    descricao = Col(String(500))
    taxa_acumulo_pontos = Col(Float, nullable=False)
    taxa_troca_pontos = Col(Float, nullable=False)
    loja_uuid = Col(String(36), ForeignKey("lojas.uuid"))
    loja = relationship("Loja", back_populates="programas_fidelidade")


class PontuacaoCliente(Base):
    __tablename__ = "pontuacao_clientes"
    uuid = Col(String(36), unique=True, primary_key=True, nullable=False)
    usuario_uuid = Col(String(36), ForeignKey("usuarios.uuid"))
    loja_uuid = Col(String(36), ForeignKey("lojas.uuid"))
    programa_fidelidade_uuid = Col(
        String(36), ForeignKey("programa_fidelidade.uuid")
    )
    pontos = Col(Float, default=0.0)
    usuario = relationship("Usuario", back_populates="pontuacoes")
    programa_fidelidade = relationship(
        "ProgramaFidelidade", back_populates="pontuacoes"
    )
