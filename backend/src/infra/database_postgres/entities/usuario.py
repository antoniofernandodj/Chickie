from src.infra.database_postgres.entities import Base
from sqlalchemy.schema import Column as Col
from sqlalchemy.types import String as Str, Text, Enum, Boolean
import enum


class ModoCadastroEnum(enum.Enum):
    importacao = 'importacao'
    cadastro_de_loja = "cadastro_de_loja"
    auto_cadastro = "auto_cadastro"


class Usuario(Base):

    __tablename__ = "usuarios"

    uuid = Col(Str(36), primary_key=True, nullable=False)
    nome = Col(Text, nullable=False)
    username = Col(Text, nullable=False, unique=True)
    email = Col(Text, nullable=False, unique=True)
    telefone = Col(Text)
    celular = Col(Text, nullable=False, unique=True)
    password_hash = Col(Text, nullable=False)
    ativo = Col(Boolean, default=True)
    passou_pelo_primeiro_acesso = Col(Boolean, default=False)

    modo_de_cadastro = Col(  # type: ignore
        Enum(ModoCadastroEnum, name="modo_de_cadastro"),
        nullable=False,
        default=ModoCadastroEnum.auto_cadastro
    )
