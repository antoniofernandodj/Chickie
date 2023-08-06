from src.infra.database.entities import Base, Usuario
from src.infra.database import session
from sqlalchemy.schema import Column as Col, ForeignKey
from sqlalchemy.types import String as Str, Text


class UsuarioNaoEncontradoException(Exception):
    pass


class LojaNaoEncontradaException(Exception):
    pass


class UsuarioJaVinculadoException(Exception):
    pass


class Loja(Base):
    __tablename__ = "lojas"

    nome = Col(Str(100))
    username = Col(Str(100))
    email = Col(Str(100))
    telefone = Col(Str(20))
    celular = Col(Str(20))
    password_hash = Col(Text)
    endereco_uuid = Col(Str(36), ForeignKey("enderecos.uuid"))

    def vincular_comprador(self, comprador: Usuario):
        from src.infra.database import entities as e

        try:
            db = session.get()

            usuario = (
                db.query(e.Usuario).filter_by(uuid=comprador.uuid).first()
            )
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
