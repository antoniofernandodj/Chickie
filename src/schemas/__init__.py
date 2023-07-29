from pydantic import BaseModel
from typing import Optional


class Usuario(BaseModel):
    
    __tablename__ = 'usuarios'
    
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    endereco_uuid: str
    password: Optional[str] = None
    password_hash: Optional[str] = None
    endereco_uuid: Optional[str] = None
    uuid: Optional[str] = None
    

class Login(BaseModel):
    password: str
    email: Optional[str] = None
    username: Optional[str] = None
    

class SignIn(BaseModel):    
    nome: str
    username: str
    email: str
    telefone: str
    celular: str
    endereco_uuid: str
    password: str
    endereco_uuid: str
