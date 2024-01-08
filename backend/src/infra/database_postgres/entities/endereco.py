from src.infra.database_postgres.entities import Base
from sqlalchemy.schema import Column as Col, ForeignKey as FK
import enum
from sqlalchemy.types import String as Str, Text, Enum


class UF(enum.Enum):
    AC = "Acre"
    AL = "Alagoas"
    AP = "Amapá"
    AM = "Amazonas"
    BA = "Bahia"
    CE = "Ceará"
    DF = "Distrito Federal"
    ES = "Espírito Santo"
    GO = "Goiás"
    MA = "Maranhão"
    MT = "Mato Grosso"
    MS = "Mato Grosso do Sul"
    MG = "Minas Gerais"
    PA = "Pará"
    PB = "Paraíba"
    PR = "Paraná"
    PE = "Pernambuco"
    PI = "Piauí"
    RJ = "Rio de Janeiro"
    RN = "Rio Grande do Norte"
    RS = "Rio Grande do Sul"
    RO = "Rondônia"
    RR = "Roraima"
    SC = "Santa Catarina"
    SP = "São Paulo"
    SE = "Sergipe"
    TO = "Tocantins"


class EnderecoLoja(Base):
    __tablename__ = "enderecos_lojas"
    uuid = Col(Str(36), unique=True, primary_key=True, nullable=False)
    uf = Col(Enum(UF))  # type: ignore
    cidade = Col(Text, nullable=False)
    logradouro = Col(Text, nullable=False)
    numero = Col(Text)
    complemento = Col(Text)
    bairro = Col(Text, nullable=False)
    cep = Col(Text)
    loja_uuid = Col(Text, FK("lojas.uuid"), nullable=False)


class EnderecoUsuario(Base):
    __tablename__ = "enderecos_usuarios"
    uuid = Col(Str(36), unique=True, primary_key=True, nullable=False)
    uf = Col(Enum(UF))  # type: ignore
    cidade = Col(Text, nullable=False)
    logradouro = Col(Text, nullable=False)
    numero = Col(Text)
    complemento = Col(Text)
    bairro = Col(Text, nullable=False)
    cep = Col(Text)
    usuario_uuid = Col(Text, FK("usuarios.uuid"), nullable=False)


class EnderecoEntrega(Base):
    __tablename__ = "enderecos_entregas"
    uuid = Col(Str(36), unique=True, primary_key=True, nullable=False)
    uf = Col(Enum(UF))  # type: ignore
    cidade = Col(Text, nullable=False)
    logradouro = Col(Text, nullable=False)
    numero = Col(Text)
    complemento = Col(Text)
    bairro = Col(Text, nullable=False)
    cep = Col(Text)
    pedido_uuid = Col(Text, FK("pedidos.uuid"), nullable=False)
