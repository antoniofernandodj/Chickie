from pydantic import BaseModel
from typing import Optional


class Funcionario(BaseModel):
    __tablename__ = "funcionarios"
    loja_uuid: str
    cargo: str
    nome: str
    username: str
    email: str
    celular: str
    
    password_hash: Optional[str] = None
    telefone: Optional[str] = None
    password: Optional[str] = None
    uuid: Optional[str] = None

    model_config = {
        'json_schema_extra': {
            'example': {
                'loja_uuid': '7613fa2f-8cde-4c66-bbb3-511a63546c9b',
                'cargo': 'Atendente',
                'nome': 'Ricardo Gomes',
                'username': 'ricardo_gomes',
                'email': 'ricardogomes@email.com',
                'telefone': '(Opcional)',
                'celular': '21965896325',
                'password': 'minha_senha'
            }
        }
    }
