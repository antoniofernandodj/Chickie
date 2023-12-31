# from src.presenters import controllers
from src.exceptions import UnauthorizedException, NotFoundException
from fastapi.routing import APIRouter
from src.api import security
from src.dependencies import (
    current_company,
    oauth2_password_request_form_dependency
)
from src.dependencies import (
    loja_repository_dependency,
    endereco_repository_dependency
)
from fastapi import HTTPException, status, Path
from typing import Any, Optional, List
from src.schemas import (
    LojaSignIn,
    Endereco,
    Token,
    Loja
)

from typing import Annotated
from src import use_cases


router = APIRouter(prefix="/loja", tags=["Loja", "Auth"])


@router.get("/{uuid}")
async def requisitar_loja(
    repository: loja_repository_dependency,
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
    result: Optional[Loja] = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException('Loja não encontrada')

    return result


@router.get("/")
async def requisitar_lojas(
    repository: loja_repository_dependency,
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
    result: List[Loja] = await repository.find_all()

    return result


@router.post("/login", response_model=Token)
async def login_post(
    form_data: oauth2_password_request_form_dependency,
    endereco_repository: endereco_repository_dependency
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
    loja = await security.authenticate_company(
        form_data.username, form_data.password
    )
    if not loja:
        raise UnauthorizedException("Incorrect username or password")

    endereco: Optional[Endereco] = await endereco_repository.find_one(
        uuid=loja.endereco_uuid
    )

    if endereco is None:
        raise NotFoundException("Endereço da loja não encontrado")

    access_token = security.create_access_token(data={"sub": loja.username})
    response = {
        "access_token": access_token,
        "token_type": "bearer",
        "uuid": loja.uuid,
        "nome": loja.nome,
        "username": loja.username,
        "email": loja.email,
        "celular": loja.celular,
        "endereco": endereco,
    }

    return response


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
    except use_cases.lojas.InvalidPasswordException:
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
