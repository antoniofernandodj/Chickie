from dataclasses import dataclass
from src.infra.database import entities as e
from src.infra.database.repository import BaseRepositoryClass
from uuid import uuid4


@dataclass
class UsuarioRepository(BaseRepositoryClass):

    model_class = e.Usuario

    @classmethod
    def create(cls, **kwargs):

        from werkzeug.security import generate_password_hash

        kwargs['uuid'] = uuid4()
        kwargs['password_hash'] = generate_password_hash(
            kwargs['password_hash']
        )

        item = cls.model_class(**kwargs)
        item.save()

        return item
