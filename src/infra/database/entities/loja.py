import enum
from src.lib.auth.classes import UserMixin
from src.infra.database.entities import BaseEntityClass
from src.infra.database.entities import Base, Usuario
from src.infra.database import session
from sqlalchemy.orm import relationship as rel
from .endereco import Endereco
from typing import Optional
from sqlalchemy.schema import Column as Col, ForeignKey as FK
from sqlalchemy.types import (
    Integer as Int, String as Str, Text, Enum
)

class UsuarioNaoEncontradoException(Exception):
    pass

class LojaNaoEncontradaException(Exception):
    pass

class UsuarioJaVinculadoException(Exception):
    pass

class Loja(Base, BaseEntityClass, UserMixin):
    
    __tablename__ = 'lojas'
    
    uuid = Col(Str(40), primary_key=True)
    nome = Col(Str(50))
    username = Col(Str(50))
    email = Col(Str(50))
    telefone = Col(Str(50))
    celular = Col(Str(50))
    password_hash = Col(Text)
    
    def vincular_comprador(self, comprador: Usuario):
        from src.infra.database import entities as e

        try:
            db = session.get()
            
            usuario = db.query(e.Usuario).filter_by(uuid=comprador.uuid).first()
            loja = db.query(e.Loja).filter_by(uuid=self.uuid).first()

            if usuario is None:
                raise UsuarioNaoEncontradoException(
                    f"Usuário com UUID {comprador.uuid} não encontrado."
                )
            
            if loja is None:
                raise LojaNaoEncontradaException(
                    f"Loja com UUID {self.uuid} não encontrada."
                )

            loja.usuarios.append(usuario)
            db.commit()
        
        finally:
            db.close()
