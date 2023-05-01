from dataclasses import dataclass
from src.infra.database import entities as e
from src.infra.database.repository import BaseRepositoryClass
from uuid import uuid4
from uuid import uuid4


@dataclass
class UsuarioRepository(BaseRepositoryClass):

    model_class = e.Usuario

    @classmethod
    def create(cls, **kwargs):
        kwargs['password_hash'] = gen_hash(kwargs['password_hash'])
        kwargs['uuid'] = uuid4()


        item = cls.model_class(**kwargs)
        item.save()
