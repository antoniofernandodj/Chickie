from dataclasses import dataclass
from src.infra.database import entities as e
from src.infra.database.repository import BaseRepositoryClass
from uuid import uuid4
from uuid import uuid4
from werkzeug.security import (
    check_password_hash as check_hash,
    generate_password_hash as gen_hash
)

@dataclass
class User(BaseRepositoryClass):

    model_class = e.User

    @classmethod
    def create(cls, **kwargs):
        kwargs['password_hash'] = gen_hash(kwargs['password_hash'])
        kwargs['uuid'] = uuid4()


        item = cls.model_class(**kwargs)
        item.save()


    def validate_credentials(user: e.User, password: str) -> bool:
        return check_hash(user.password_hash, password)