from typing import Any, Annotated

from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.requests import Request

from src.api import security
from src.schemas import Token, UsuarioSignIn
from src import use_cases
from src.schemas import Loja, Usuario
from typing import Annotated
from src.api import security


current_user = Annotated[Usuario, Depends(security.current_user)]
current_company = Annotated[Loja, Depends(security.current_company)]


router = APIRouter(prefix="/user", tags=["Usuario", "Auth"])


@router.post("/login", response_model=Token)
async def login_post(
    request: Request,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Any:
    """
    Realiza o login de um usuário.
    
    Args:
        request (Request): O objeto de requisição HTTP.
        form_data (OAuth2PasswordRequestForm): Dados do formulário de login.
    
    Returns:
        dict: Um dicionário contendo o token de acesso e o uuid do usuário.
    
    Raises:
        HTTPException: Se as credenciais forem inválidas.
    """
    user = await security.authenticate_user(
        form_data.username, form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = security.create_access_token(data={"sub": user.username})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "uuid": user.uuid,
    }


# Adicionar verificação para unico
# Tbm no banco
@router.post("/signin", status_code=status.HTTP_201_CREATED)
async def signin(usuario: UsuarioSignIn) -> Any:
    """
    Realiza o cadastro de um novo usuário.
    
    Args:
        usuario (UsuarioSignIn): Os detalhes do usuário a ser cadastrado.
    
    Returns:
        dict: Um dicionário contendo o uuid do usuário cadastrado.
    """
    try:
        uuid = await use_cases.usuarios.registrar(user_data=usuario)
    except use_cases.usuarios.UnvalidPasswordException:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Senha inválida! A senha deve ser maior que 5"
        )

    return {"uuid": uuid}


@router.get("/protected")
async def home(current_user: current_user):
    """
    Rota de exemplo protegida por autenticação.
    
    Args:
        current_user (Usuario): O objeto do usuário autenticado.
    
    Returns:
        dict: Uma mensagem de resposta.
    """
    return {"msg": "ok"}
