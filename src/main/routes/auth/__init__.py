from src.presenters import controllers
from fastapi.routing import APIRouter
from src.infra.database.repositories import UsuarioRepository, Usuario
from src.infra.database.config import DatabaseService
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
from fastapi import status
from typing import Optional, Any
from src.schemas import Login, SignIn



router = APIRouter(prefix='')


@router.post('/login', response_model=Usuario)
async def login_post(login: Login) -> Any:
    async with DatabaseService() as connection:
        user_repo = UsuarioRepository(connection=connection)
        
        u1 = await user_repo.find_one(username=login.username)
        u2 = await user_repo.find_one(email=login.email)
        user: Optional[Usuario] = u1 or u2
        if not user or not isinstance(user, Usuario):
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                'user not found'
            )
        auth = user_repo.authenticate(user, login.password)
            
    del user.password
    return user


@router.post('/signin')
async def signin(usuario: SignIn) -> Any:
    async with DatabaseService() as connection:
        user_repo = UsuarioRepository(connection=connection)
        uuid = await user_repo.register(usuario)
        return {'uuid': uuid}
