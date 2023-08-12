# from src.presenters import controllers
from datetime import timedelta
from typing import Any, Annotated

from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.requests import Request

from src.api import security
from src.schemas import Usuario
from src.schemas import Token, UsuarioSignIn
from config import settings as s
from src import use_cases


router = APIRouter(prefix="/user", tags=["Usuario", "Auth"])
current_user = Annotated[Usuario, Depends(security.current_user)]


@router.post("/login", response_model=Token)
async def login_post(
    request: Request,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
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
        "uuid": user.uuid,
    }


# Adicionar verificação para unico
# Tbm no banco
@router.post("/signin", status_code=status.HTTP_201_CREATED)
async def signin(usuario: UsuarioSignIn) -> Any:
    uuid = await use_cases.usuarios.registrar(user_data=usuario)
    return {"uuid": uuid}


@router.get("/protected")
async def home(current_user: current_user):
    return {"msg": "ok"}
