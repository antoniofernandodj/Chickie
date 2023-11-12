from pydantic import BaseModel
from typing import Optional
import base64
import bcrypt


class Loja(BaseModel):
    __tablename__ = "lojas"
    nome: str
    username: str
    email: str
    celular: str
    password_hash: str

    telefone: Optional[str] = None
    endereco_uuid: Optional[str] = None
    password: Optional[str] = None
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'nome': 'Loja',
                    'username': 'loja',
                    'email': 'loja@email.com',
                    'telefone': '2127698847',
                    'celular': '21987452123'
                }, {
                    'nome': 'Loja',
                    'username': 'loja',
                    'email': 'loja@email.com',
                    'celular': '21987452123'
                }
            ]
        }
    }
    
    def authenticate(self, senha_loja: str) -> bool:
        if self.password_hash is None:
            raise

        hash_bytes = base64.b64decode(self.password_hash.encode("utf-8"))
        return bcrypt.checkpw(senha_loja.encode("utf-8"), hash_bytes)

