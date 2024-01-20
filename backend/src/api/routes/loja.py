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
from src.dependencies import (
    oauth2_password_request_form_dependency
)
from fastapi import (
    HTTPException,
    status,
    Path,
    Response,
    Query,
    Request,
    Depends
)
from typing import Any, Optional, List, Dict, Annotated
from src.domain.models import (
    Cliente,
    UsuarioSignUp,
    LojaSignUp,
    LojaPUT,
    # Endereco,
    LojaAuthData,
    Loja,
    Produto,
    Lojas,
    LojaGET,
    ProdutoGET,
    LojaUpdateImageCadastro,
    UsuarioFollowEmpresaRequest
)
from src.services import (
    ImageUploadService,
    ImageUploadServiceResponse,
)
from src.domain.services import ProdutoService, LojaService
from src.api.security import oauth2_scheme, AuthService
from src import use_cases  # noqa
from aiopg import Connection
from src.misc import Paginador  # noqa
from src.dependencies import ConnectionDependency


router = APIRouter(prefix="/loja", tags=["Loja"])


@router.get(
    "/{uuid}"
)
async def requisitar_loja(
    request: Request,
    uuid: Annotated[str, Path(title="O uuid da loja a fazer get")]
) -> LojaGET:

    connection: Connection = request.state.connection

    service = LojaService(connection)
    repository = Repository(Loja, connection=connection)

    loja: Optional[Loja] = await repository.find_one(uuid=uuid)
    if loja is None:
        raise NotFoundException('Loja não encontrada')

    response = await service.get_data(loja)
    return response


@router.get(
    "/"
)
async def requisitar_lojas(
    request: Request,
    limit: int = Query(0),
    offset: int = Query(1),
) -> Lojas:

    connection: Connection = request.state.connection

    service = LojaService(connection)
    repository = Repository(Loja, connection=connection)
    result: List[LojaGET] = []
    lojas: List[Loja] = await repository.find_all()
    for loja in lojas:
        loja_data = await service.get_data(loja)
        result.append(loja_data)

    paginate = Paginador(result, offset, limit)
    return Lojas(**paginate.get_response())


@router.post(
    "/login",
    tags=["Auth"],
    response_model=LojaAuthData
)
async def login(
    form_data: oauth2_password_request_form_dependency,
    connection: Connection = Depends(connection),
) -> Any:

    # connection: Connection = request.state.connection

    service = LojaService(connection)
    auth_service = AuthService(connection)
    loja = await auth_service.authenticate_company(
        form_data.username, form_data.password
    )
    if not loja:
        raise UnauthorizedException("Credenciais inválidas!")

    access_token = AuthService.create_access_token({"sub": loja.username})

    loja_data = await service.get_data(loja)

    return LojaAuthData(
        access_token=access_token,
        token_type='bearer',
        loja=loja_data
    )


@router.put("/{uuid}", summary='Atualizar dados de cadastro da Loja')
async def update_loja(
    request: Request,
    updated_data: LojaPUT,
    uuid: Annotated[str, Path(title="O uuid da loja a ser atualizada")]
):

    connection: Connection = request.state.connection

    service = LojaService(connection)
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
    tags=["Auth"],
    status_code=status.HTTP_201_CREATED
)
async def signup(request: Request, loja: LojaSignUp) -> Any:

    connection: Connection = request.state.connection

    service = LojaService(connection)
    try:
        loja_cadastrada = await service.registrar(loja_data=loja)

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
    request: Request,
    loja_uuid: str,
    categoria_uuid: str
) -> List[ProdutoGET]:

    connection: Connection = request.state.connection

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


@router.post(
    '/imagem_cadastro',
    summary="Atualizar imagem de cadastro da loja",
    responses={
        404: {"description": "Loja não encontrada"}
    }
)
async def atualizar_imagem_de_cadastro(
    request: Request,
    token: Annotated[str, Depends(oauth2_scheme)],
    image: LojaUpdateImageCadastro
) -> Dict[str, ImageUploadServiceResponse]:

    connection: Connection = request.state.connection

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)
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
        import traceback
        traceback.print_exc()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro no upload da imagem! Detalhes: {error}"
        )


@router.delete(
    '/imagem_cadastro',
    summary="Remover imagem de cadastro da loja",
    responses={
        404: {"description": "Loja não encontrada"}
    }
)
async def remover_imagem_de_cadastro(
    request: Request,
    token: Annotated[str, Depends(oauth2_scheme)],
    image: LojaUpdateImageCadastro
):

    connection: Connection = request.state.connection

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)
    try:
        image_service = ImageUploadService(loja=loja)
        image_service.delete_image_cadastro()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro na Remoção da imagem! Detalhes: {error}"
        )


@router.patch(
    "/ativar_inativar/{uuid}"
)
async def ativar_inativar_loja(
    request: Request,
    uuid: Annotated[str, Path(title="O uuid da loja a ativar/inativar")],
    ativar: bool
) -> Any:

    connection: Connection = request.state.connection

    loja_repository = Repository(Loja, connection)
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
    request: Request,
    uuid: Annotated[str, Path(title="O uuid da loja a ser deletada")]
) -> Any:

    return {"message": "Loja deletada com sucesso!"}


@router.post("/cliente", status_code=status.HTTP_201_CREATED)
async def cadastrar_cliente(
    request: Request,
    token: Annotated[str, Depends(oauth2_scheme)],
    usuario: UsuarioFollowEmpresaRequest
) -> Any:

    connection: Connection = request.state.connection
    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa

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
    request: Request,
    token: Annotated[str, Depends(oauth2_scheme)],
    usuario: UsuarioSignUp,
    loja_uuid: str
) -> Any:

    connection: Connection = request.state.connection
    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa

    try:
        usuario_cadastrado = await use_cases.usuarios.registrar(
            user_data=usuario, connection=connection
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
    request: Request,
    token: Annotated[str, Depends(oauth2_scheme)],
    complete: str = Query('0')
):

    connection: Connection = request.state.connection

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)
    service = LojaService(connection)
    access_token = AuthService.create_access_token({"sub": loja.username})

    loja_data = None

    if complete == '1':
        loja_data = await service.get_data(loja)

    return LojaAuthData(
        access_token=access_token,
        token_type='bearer',
        loja=loja_data
    )
