from pydantic import BaseModel
from typing import Optional
import base64
import bcrypt


class Loja(BaseModel):
    __tablename__ = "lojas"
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    password_hash: str

    endereco_uuid: Optional[str] = None
    password: Optional[str] = None
    uuid: Optional[str] = None

    def authenticate(self, senha_loja: str) -> bool:
        if self.password_hash is None:
            raise
        hash_bytes = base64.b64decode(self.password_hash.encode("utf-8"))
        return bcrypt.checkpw(senha_loja.encode("utf-8"), hash_bytes)
