from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    nome: str
    username: str
    email: str
    uuid: str | None = None


class TokenData(BaseModel):
    username: str | None = None
