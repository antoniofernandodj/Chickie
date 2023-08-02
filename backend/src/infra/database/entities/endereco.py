from src.infra.database.entities import BaseEntityClass
from src.infra.database.entities import Base
from sqlalchemy.schema import Column as Col
import enum
from sqlalchemy.types import (
    Integer as Int, String as Str, Text, Enum, Float
)


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


class Endereco(Base, BaseEntityClass):
    
    __tablename__ = 'enderecos'
    
    uuid = Col(Str(40), primary_key=True)
    uf = Col(Enum(UF))
    cidade = Col(Str(50))
    logradouro = Col(Text)
    numero = Col(Str(50))
    complemento = Col(Str(50))
    bairro = Col(Text)
    cep = Col(Str(50))
    timestamp = Col(Float)
