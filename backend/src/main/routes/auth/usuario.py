# from src.presenters import controllers
from datetime import timedelta
from typing import Any, Annotated

from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from fastapi.requests import Request

from src.main import security
from src.infra.database.repositories import UsuarioRepository
from src.infra.database.config import DatabaseConnectionManager
from src.schemas import Usuario
from src.schemas import Token, UsuarioSignIn
from config import settings as s



router = APIRouter(
    prefix='/user',
    tags=['Usuario Auth']
)
current_user = Annotated[Usuario, Depends(security.current_user)]


@router.post('/login', response_model=Token)
async def login_post(
        request: Request,
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    ) -> Any:
    
    user = await security.authenticate_user(
        form_data.username, form_data.password
    )
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=s.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "uuid": user.uuid
    }


@router.post('/signin', status_code=status.HTTP_201_CREATED)
async def signin(usuario: UsuarioSignIn) -> Any:
    async with DatabaseConnectionManager() as connection:
        user_repo = UsuarioRepository(connection=connection)
        uuid = await user_repo.register(usuario)
        return {'uuid': uuid}


@router.get('/protected')
async def home(current_user: current_user):
    
    return {
        'msg': 'ok'
    }