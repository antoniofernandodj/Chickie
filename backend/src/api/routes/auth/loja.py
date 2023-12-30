# from src.presenters import controllers
from fastapi.routing import APIRouter
from src.api import security
from src.infra.database_postgres.manager import DatabaseConnectionManager
from src.infra.database_postgres.repository import Repository
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status, Path
from typing import Any
from src.schemas import (
    LojaSignIn,
    Usuario,
    Token,
    Loja,
    # UsuarioSignIn,
    # Cliente
)

from typing import Annotated
from src import use_cases
from fastapi import (  # noqa
    Depends
)


current_user = Annotated[Usuario, Depends(security.current_user)]
current_company = Annotated[Loja, Depends(security.current_company)]


router = APIRouter(prefix="/loja", tags=["Loja", "Auth"])


NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
)


@router.get("/{uuid}")
async def requisitar_loja(
    uuid: Annotated[str, Path(title="O uuid da loja a fazer get")]
):
    """
    Busca uma loja pelo seu uuid.

    Args:
        uuid (str): O uuid da loja a ser buscada.

    Returns:
        Loja: A loja encontrada.

    Raises:
        HTTPException: Se a loja não for encontrada.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Loja, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/login", response_model=Token)
async def login_post(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Any:
    """
    Realiza o login de uma loja.

    Args:
        form_data (OAuth2PasswordRequestForm): Dados do formulário de login.

    Returns:
        dict: Um dicionário contendo o token de acesso e o uuid da loja.

    Raises:
        HTTPException: Se as credenciais forem inválidas.
    """
    user = await security.authenticate_company(
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
        "nome": user.nome,
        "username": user.username,
        "email": user.email,
    }


# Adicionar verificação para unico
# Tbm no banco
@router.post("/signin", status_code=status.HTTP_201_CREATED)
async def signin(loja: LojaSignIn) -> Any:
    """
    Realiza o cadastro de uma nova loja.

    Args:
        loja (LojaSignIn): Os detalhes da loja a ser cadastrada.

    Returns:
        dict: Um dicionário contendo o uuid da loja cadastrada.
    """
    try:
        uuid = await use_cases.lojas.registrar(loja_data=loja)
    except use_cases.lojas.UnvalidPasswordException:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Senha inválida! A senha deve ser maior que 5"
        )

    return {"uuid": uuid}


@router.get("/protected")
async def home(current_company: current_company):
    """
    Rota de exemplo protegida por autenticação.

    Args:
        current_company (Loja): O objeto da loja autenticada.

    Returns:
        dict: Uma mensagem de resposta.
    """
    return {"msg": "ok"}


# @router.post("/cliente", status_code=status.HTTP_201_CREATED)
# async def cadastrar_cliente(
#     current_company: current_company, usuario: UsuarioSignIn
# ) -> Any:
#     """
#     Cadastra um novo cliente associado à loja autenticada.

#     Args:
#         current_company (Loja): O objeto da loja autenticada.
#         usuario (UsuarioSignIn): Os detalhes do cliente a ser cadastrado.

#     Returns:
#         dict: Um dicionário contendo o uuid do usuário (cliente) cadastrado.

#     Raises:
#         HTTPException: Se não for fornecido o uuid da loja.
#     """
#     if usuario.loja_uuid is None:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="uuid da loja em falta",
#         )

#     usuario_uuid = await use_cases.usuarios.registrar(user_data=usuario)
#     cliente = Cliente(usuario_uuid=usuario_uuid, loja_uuid=usuario.loja_uuid)
#     async with DatabaseConnectionManager() as connection:
#         repository = Repository(Cliente, connection=connection)
#         await repository.save(cliente)

#     return {"uuid": usuario_uuid}
