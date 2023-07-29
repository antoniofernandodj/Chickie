import asyncio
from src.schemas import Usuario, UsuarioSignIn
from src.infra.database.repositories import BaseRepositoryClass, UserMixin
import base64
import bcrypt



class UsuarioRepository(BaseRepositoryClass, UserMixin):

    def __init__(self, connection):
        super().__init__(connection=connection)
        self.__tablename__ = 'usuarios'
        self.lock = asyncio.Lock()
        self.model = Usuario
        
    async def register(self, user_data: UsuarioSignIn):
        salt = bcrypt.gensalt()
        password: str = user_data.password
        user_data_dict = user_data.model_dump()
        hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        hash_base64 = base64.b64encode(hash).decode('utf-8')
        user_data_dict['password_hash'] = hash_base64
        user = Usuario(**user_data_dict)
        del user.password
        del user_data
        
        return await self.save(user)
