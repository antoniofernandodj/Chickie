from pydantic import BaseModel
from src.schemas import Endereco


class Token(BaseModel):
    access_token: str
    token_type: str
    nome: str
    username: str
    email: str
    endereco: Endereco
    celular: str | None = None
    uuid: str | None = None


class TokenData(BaseModel):
    username: str | None = None
