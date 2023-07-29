# from src.presenters import controllers
from fastapi.routing import APIRouter
from fastapi import Depends
from datetime import timedelta
from src.main import security
from src.infra.database.repositories import LojaRepository
from src.schemas import Usuario
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.infra.database.config import DatabaseConnectionManager
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
from fastapi import Depends, FastAPI, HTTPException, status
from typing import Optional, Any
from src.schemas import Login, LojaSignIn, Token, Loja
from typing import Annotated
from config import settings as s


router = APIRouter(
    prefix='/loja',
    tags=['Loja Auth']
)
current_company = Annotated[Loja, Depends(security.current_company)]


@router.post('/login', response_model=Token)
async def login_post(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    ) -> Any:
    
    user = await security.authenticate_company(
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
async def signin(loja: LojaSignIn) -> Any:
    async with DatabaseConnectionManager() as connection:
        loja_repo = LojaRepository(connection=connection)
        uuid = await loja_repo.register(loja)
        return {'uuid': uuid}


@router.get('/protected')
async def home(current_company: current_company):
    
    return {
        'msg': 'ok'
    }