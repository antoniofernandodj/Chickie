from pydantic import BaseModel
from typing import Optional
# from src.schemas import Endereco
import base64
import bcrypt


class LojaGETResponse(BaseModel):
    __tablename__ = "lojas"
    nome: str
    username: str
    email: str
    celular: str
    uuid: str
    # endereco: Endereco
    telefone: Optional[str] = None
    imagem_cadastro: Optional[str] = None
    horarios_de_funcionamento: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'nome': 'Loja',
                    'username': 'loja',
                    'email': 'loja@email.com',
                    'telefone': '2127698847',
                    'celular': '21987452123',
                    'horarios_de_funcionamento': 'Seg a Sáb, até 19h'
                }, {
                    'nome': 'Loja',
                    'username': 'loja',
                    'email': 'loja@email.com',
                    'celular': '21987452123',
                    'horarios_de_funcionamento': 'Seg a Sáb, até 19h'
                }
            ]
        }
    }


class Loja(BaseModel):
    __tablename__ = "lojas"
    nome: str
    username: str
    email: str
    celular: str
    password_hash: str

    telefone: Optional[str] = None
    password: Optional[str] = None
    uuid: Optional[str] = None
    ativo: Optional[bool] = True
    passou_pelo_primeiro_acesso: Optional[bool] = False
    horarios_de_funcionamento: Optional[str] = None

    def authenticate(self, senha_loja: str) -> bool:
        if self.password_hash is None:
            raise

        hash_bytes = base64.b64decode(self.password_hash.encode("utf-8"))
        return bcrypt.checkpw(senha_loja.encode("utf-8"), hash_bytes)
