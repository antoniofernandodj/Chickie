# from src.presenters import controllers
from src.infra.database_postgres.repository import Repository
from src.exceptions import (
    UnauthorizedException,
    NotFoundException,
    ConflictException,
    LojaJaCadastradaException,
    InvalidPasswordException
)

from fastapi.routing import APIRouter
from src.api import security
from src.dependencies import (
    current_company,
    oauth2_password_request_form_dependency
)
from src.dependencies import (  # noqa
    loja_repository_dependency,
    loja_service_dependency
)

from src.dependencies.connection_dependency import connection_dependency
from fastapi import HTTPException, status, Path, Response, Query
from typing import Any, Optional, List, Dict
from src.models import (
    Cliente,
    UsuarioSignUp,
    LojaSignUp,
    LojaPUT,
    # Endereco,
    LojaToken,
    Loja,
    Produto,
    LojaGET,
    ProdutoGET,
    LojaUpdateImageCadastro,
    UsuarioFollowEmpresaRequest
)
from src.services import (
    ImageUploadService,
    ImageUploadServiceResponse,
    ProdutoService
)


from typing import Annotated
from src import use_cases  # noqa


router = APIRouter(prefix="/loja", tags=["Loja", "Auth"])


@router.get(
    "/{uuid}"
)
async def requisitar_loja(
    loja_service: loja_service_dependency,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid da loja a fazer get")]
) -> LojaGET:
    """
    Busca uma loja pelo seu uuid.

    Args:
        uuid (str): O uuid da loja a ser buscada.

    Returns:
        Loja: A loja encontrada.

    Raises:
        HTTPException: Se a loja não for encontrada.
    """

    repository = Repository(Loja, connection=connection)

    loja: Optional[Loja] = await repository.find_one(uuid=uuid)
    if loja is None:
        raise NotFoundException('Loja não encontrada')

    response = await loja_service.get_data(loja)

    return response


@router.get(
    "/"
)
async def requisitar_lojas(
    connection: connection_dependency,
    loja_service: loja_service_dependency,
) -> List[LojaGET]:
    """
    Busca uma loja pelo seu uuid.

    Args:
        uuid (str): O uuid da loja a ser buscada.

    Returns:
        Loja: A loja encontrada.

    Raises:
        HTTPException: Se a loja não for encontrada.
    """

    repository = Repository(Loja, connection=connection)
    response: List[LojaGET] = []
    lojas: List[Loja] = await repository.find_all()
    for loja in lojas:
        loja_data = await loja_service.get_data(loja)
        response.append(loja_data)

    return response


@router.post(
    "/login",
    response_model=LojaToken
)
async def login(
    form_data: oauth2_password_request_form_dependency,
    loja_service: loja_service_dependency,
    connection: connection_dependency
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
        raise UnauthorizedException("Credenciais inválidas!")

    access_token = security.create_access_token(
        data={"sub": loja.username}
    )

    loja_data = await loja_service.get_data(loja)

    return LojaToken(
        access_token=access_token,
        token_type='bearer',
        loja=loja_data
    )


@router.put("/{uuid}", summary='Atualizar dados de cadastro da Loja')
async def update_loja(
    service: loja_service_dependency,
    connection: connection_dependency,
    updated_data: LojaPUT,
    uuid: Annotated[str, Path(title="O uuid da loja a ser atualizada")]
):
    """
    Atualiza os detalhes de uma loja existente.

    Args:
        `uuid` (str): O uuid da loja a ser atualizada.
        `updated_data` (LojaPUT): Os novos detalhes da loja.

    Returns:
        `dict`: Um dicionário confirmando a atualização.

    Raises:
        `HTTPException`: Se a loja não for encontrada ou ocorrer um erro na atualização.  # noqa
    """

    try:
        await service.update_loja_data(uuid, updated_data)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao atualizar a loja! Detalhes: {error}"
        )


@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED
)
async def signup(
    loja: LojaSignUp,
    loja_service: loja_service_dependency
) -> Any:
    """
    Realiza o cadastro de uma nova loja.

    Args:
        loja (LojaSignUp): Os detalhes da loja a ser cadastrada.

    Returns:
        dict: Um dicionário contendo o uuid da loja cadastrada.
    """
    try:
        loja_cadastrada = await loja_service.registrar(loja_data=loja)

    except InvalidPasswordException:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Senha inválida! A senha deve ser maior que 5"
        )

    except LojaJaCadastradaException:
        raise ConflictException(detail="Credenciais inválidas!")

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro no cadastro da loja! detail: {error}"
        )

    return {"uuid": loja_cadastrada.uuid}


@router.get("/{loja_uuid}/produtos")
async def requisitar_produtos_de_loja(
    connection: connection_dependency,
    loja_uuid: str,
    categoria_uuid: str
) -> List[ProdutoGET]:

    """
    Requisita os produtos de uma loja específica
    cadastrados na plataforma.
    Aceita um uuid como query para buscar os
    produtos de uma empresa específica

    Args:
        loja_uuid (Optional[str]): O uuid da empresa,
        caso necessário

    Returns:
        list[Produto]
    """
    loja_repository = Repository(Loja, connection=connection)
    produto_repository = Repository(Produto, connection=connection)
    loja: Optional[Loja] = await loja_repository.find_one(
        uuid=loja_uuid
    )
    if loja is None:
        raise NotFoundException('Loja de produto não encontrada!')
    produto_service = ProdutoService(connection=connection)

    kwargs = {}
    if categoria_uuid is not None:
        kwargs["categoria_uuid"] = categoria_uuid

    response = []
    produtos: List[Produto] = await produto_repository.find_all(**kwargs)
    for produto in produtos:
        precos = await produto_service.get_precos(produto)
        try:
            image_url = await produto_service.get_public_url_image(produto)
        except ValueError:
            image_url = None
        response_item = ProdutoGET(
            uuid=produto.uuid,
            nome=produto.nome,
            descricao=produto.nome,
            preco=produto.preco,
            categoria_uuid=produto.categoria_uuid,
            loja_uuid=produto.loja_uuid,
            precos=precos,
            image_url=image_url
        )
        response.append(response_item)
    return response


@router.patch(
    '/atualizar_imagem_cadastro',
    summary="Atualizar imagem de cadastro da loja",
    responses={
        404: {"description": "Loja não encontrada"}
    }
)
async def atualizar_imagem_de_cadastro(
    loja: current_company,
    image: LojaUpdateImageCadastro
) -> Dict[str, ImageUploadServiceResponse]:
    """
    Atualiza a imagem de cadastro de uma loja.

    Args:
    - `uuid` (str): O UUID da loja a ser atualizada na imagem de cadastro.
    - `image` (LojaUpdateImageCadastro): Detalhes da imagem a ser atualizada.

    Returns:
    - `JSONResponse`: Retorna um JSON vazio com um status code de 204 se a atualização for bem-sucedida.  # noqa

    Raises:
    - `HTTPException`: Se ocorrer um erro durante o upload da imagem.
    """

    try:
        image_service = ImageUploadService(loja=loja)
        try:
            image_bytes_base64 = image.bytes_base64.split(',')[1]
        except IndexError:
            image_bytes_base64 = image.bytes_base64

        result = image_service.upload_image_cadastro(
            base64_string=image_bytes_base64,
            filename=image.filename
        )
        return {'result': result}

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro no upload da imagem! Detalhes: {error}"
        )


@router.get(
    "/protected"
)
async def home(current_company: current_company):
    """
    Rota de exemplo protegida por autenticação.

    Args:
        current_company (Loja): O objeto da loja autenticada.

    Returns:
        dict: Uma mensagem de resposta.
    """
    return {"msg": "ok"}


@router.patch(
    "/ativar_inativar/{uuid}"
)
async def ativar_inativar_loja(
    loja_repository: loja_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid da loja a ativar/inativar")],
    ativar: bool
) -> Any:
    """
    Ativa ou inativa uma loja baseada no UUID.

    Args:
        uuid (str): O UUID da loja a ativar/inativar.
        ativar (bool): Define se a loja será ativada (True) ou inativada (False).  # noqa

    Returns:
        dict: Uma mensagem de confirmação.

    Raises:
        HTTPException: Se a loja não for encontrada.
    """
    loja: Optional[Loja] = await loja_repository.find_one(uuid=uuid)
    if loja is None:
        raise NotFoundException('Loja não encontrada')

    await loja_repository.update(loja, {'ativo': ativar})

    status_msg = "ativada" if ativar is True else "inativada"
    return {"message": f"Loja {status_msg} com sucesso!"}


@router.delete(
    "/{uuid}"
)
async def deletar_loja(
    uuid: Annotated[str, Path(title="O uuid da loja a ser deletada")]
) -> Any:
    """
    Deleta uma loja baseada no UUID.

    Args:
        uuid (str): O UUID da loja a ser deletada.

    Returns:
        dict: Uma mensagem de confirmação.

    Raises:
        HTTPException: Se a loja não for encontrada.
    """

    return {"message": "Loja deletada com sucesso!"}


@router.post("/cliente", status_code=status.HTTP_201_CREATED)
async def cadastrar_cliente(
    connection: connection_dependency,
    current_company: current_company,
    usuario: UsuarioFollowEmpresaRequest
) -> Any:
    """
    Cadastra um novo cliente associado à loja autenticada.

    Args:
        current_company (Loja): O objeto da loja autenticada.
        usuario (UsuarioFollowEmpresaRequest): Os detalhes do cliente a ser cadastrado.  # noqa

    Returns:
        dict: Um dicionário contendo o uuid do usuário (cliente) cadastrado.

    Raises:
        HTTPException: Se não for fornecido o uuid da loja.
    """
    if usuario.loja_uuid is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="uuid da loja em falta",
        )

    cliente = Cliente(
        usuario_uuid=usuario.usuario_uuid,
        loja_uuid=usuario.loja_uuid
    )

    cliente_repository = Repository(Cliente, connection=connection)
    cliente_uuid = await cliente_repository.save(cliente)

    return {"uuid": cliente_uuid}


@router.post("/cliente_v2/{loja_uuid}", status_code=status.HTTP_201_CREATED)
async def cadastrar_cliente_v2(
    connection: connection_dependency,
    current_company: current_company,
    usuario: UsuarioSignUp,
    loja_uuid: str
) -> Any:
    """
    Cadastra um novo cliente associado à loja autenticada.

    Args:
        current_company (Loja): O objeto da loja autenticada.
        usuario (UsuarioSignUp): Os detalhes do cliente a ser cadastrado.

    Returns:
        dict: Um dicionário contendo o uuid do usuário (cliente) cadastrado.

    Raises:
        HTTPException: Se não for fornecido o uuid da loja.
    """

    try:
        usuario_cadastrado = await use_cases.usuarios.registrar(
            user_data=usuario
        )
    except use_cases.usuarios.InvalidPasswordException:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Senha inválida! A senha deve ser maior que 5"
        )

    if usuario_cadastrado.uuid is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro no cadastro de usuário: usuario_uuid nulo"
        )

    cliente = Cliente(
        usuario_uuid=usuario_cadastrado.uuid,
        loja_uuid=loja_uuid
    )

    cliente_repository = Repository(Cliente, connection=connection)
    cliente_uuid = await cliente_repository.save(cliente)

    return {
        "usuario_uuid": usuario_cadastrado.uuid,
        "cliente_uuid": cliente_uuid
    }


@router.post('/refresh')
async def refresh(
    loja: current_company,
    service: loja_service_dependency,
    complete: str = Query('0')
):
    access_token = security.create_access_token(
        data={"sub": loja.username}
    )

    loja_data = None

    if complete == '1':
        loja_data = await service.get_data(loja)

    return LojaToken(
        access_token=access_token,
        token_type='bearer',
        loja=loja_data
    )
