import bcrypt
import base64
import asyncio
from src.schemas import LojaSignIn, Loja
from src.infra.database.repositories import (
    BaseRepositoryClass, UserMixin
)


class LojaRepository(BaseRepositoryClass, UserMixin):

    def __init__(self, connection):
        super().__init__(connection=connection)
        self.__tablename__ = 'lojas'
        self.lock = asyncio.Lock()
        self.model = Loja

    async def register(self, loja_data: LojaSignIn):
        salt = bcrypt.gensalt()
        password: str = loja_data.password
        loja_data_dict = loja_data.model_dump()
        hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        hash_base64 = base64.b64encode(hash).decode('utf-8')
        loja_data_dict['password_hash'] = hash_base64
        loja = Loja(**loja_data_dict)
        del loja.password
        del loja_data
        
        return await self.save(loja)
