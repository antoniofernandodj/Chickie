# from src.presenters import controllers
from fastapi.routing import APIRouter
from datetime import timedelta
from src.main import security
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from typing import Any
from src.schemas import LojaSignIn, Token, Loja
from typing import Annotated
from config import settings as s
from src import use_cases


router = APIRouter(prefix="/loja", tags=["Loja", "Auth"])
current_company = Annotated[Loja, Depends(security.current_company)]


@router.post("/login", response_model=Token)
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
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "uuid": user.uuid,
    }


# Adicionar verificação para unico
# Tbm no banco
@router.post("/signin", status_code=status.HTTP_201_CREATED)
async def signin(loja: LojaSignIn) -> Any:
    uuid = await use_cases.lojas.registrar(loja_data=loja)
    return {"uuid": uuid}


@router.get("/protected")
async def home(current_company: current_company):
    return {"msg": "ok"}
