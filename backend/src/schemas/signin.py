from pydantic import BaseModel


class UsuarioSignIn(BaseModel):
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    endereco_uuid: str
    password: str


class LojaSignIn(BaseModel):
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    password: str
