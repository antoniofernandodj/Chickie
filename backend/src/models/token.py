from pydantic import BaseModel
from src.models import EnderecoUsuario, LojaGET


class Token(BaseModel):
    access_token: str
    token_type: str
    nome: str
    username: str
    email: str
    endereco: EnderecoUsuario
    celular: str | None = None
    uuid: str | None = None


class LojaToken(BaseModel):
    access_token: str
    token_type: str
    loja: LojaGET | None = None
