from src.presenters import controllers
from fastapi.routing import APIRouter
from fastapi import Depends
from datetime import timedelta
from src.main import security
from src.infra.database.repositories import UsuarioRepository, Usuario
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.infra.database.config import DatabaseService
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
from fastapi import Depends, FastAPI, HTTPException, status
from typing import Optional, Any
from src.schemas import Login, SignIn, Token
from typing import Annotated
from config import settings as s


router = APIRouter(prefix='')


current_user = Annotated[Usuario, Depends(security.current_user)]


@router.post('/login', response_model=Token)
async def login_post(
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
    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/signin', status_code=status.HTTP_201_CREATED)
async def signin(usuario: SignIn) -> Any:
    async with DatabaseService() as connection:
        user_repo = UsuarioRepository(connection=connection)
        uuid = await user_repo.register(usuario)
        return {'uuid': uuid}


@router.get('/protected')
async def home(current_user: current_user):
    
    return {
        'msg': 'ok'
    }