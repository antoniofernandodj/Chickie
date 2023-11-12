from pydantic import BaseModel
from typing import Optional
import base64
import bcrypt


class Usuario(BaseModel):
    __tablename__ = "usuarios"
    nome: str
    username: str
    email: str
    celular: str
    endereco_uuid: str

    telefone: Optional[str] = None
    password: Optional[str] = None
    password_hash: Optional[str] = None
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'nome': 'Pedro Almeida',
                'username': 'pedroalmeida',
                'email': 'pedroalmeida@email.com',
                'telefone': None,
                'celular': '21965236587',
                'password': 'gjhn348hgtfwr',
                'endereco_uuid': '8077977c-c5d2-4660-af39-5a15d5f3d565',
            }
        }
    }

    def authenticate(self, senha_usuario: str) -> bool:
        """
        Autentica a senha do usuário comparando-a com o hash armazenado.

        Args:
            senha_usuario (str): A senha fornecida pelo usuário.

        Returns:
            bool: True se a senha estiver correta, False caso contrário.
        """
        if self.password_hash is None:
            raise
        hash_bytes = base64.b64decode(self.password_hash.encode("utf-8"))
        return bcrypt.checkpw(senha_usuario.encode("utf-8"), hash_bytes)

