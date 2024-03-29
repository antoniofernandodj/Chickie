# from src.presenters import controllers
from src.infra.database_postgres.handlers import QueryHandler, CommandHandler
from src.exceptions import (
    UnauthorizedException,
    NotFoundException,
    ConflictException,
    LojaJaCadastradaException,
    InvalidPasswordException
)
from fastapi.routing import APIRouter
from src import dependencies
from fastapi import (
    HTTPException,
    status,
    Path,
    Response,
    Query
)
from typing import Any, Optional, List, Dict, Annotated
from src.domain.models import (  # noqa
    Cliente,
    Usuario,
    UsuarioGET,
    EnderecoUsuario,
    UsuarioSignUp,
    LojaSignUp,
    LojaPUT,
    # Endereco,
    LojaAuthData,
    Loja,
    Produto,
    Produtos,
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
# from src.domain.services import ProdutoService
from src.api.security import AuthService
from src.misc import Paginador  # noqa


router = APIRouter(prefix="/loja", tags=["Loja"])


@router.get(
    "/{uuid}"
)
async def requisitar_loja(
    connection: dependencies.ConnectionDependency,
    service: dependencies.LojaServiceDependency,
    uuid: Annotated[str, Path(title="O uuid da loja a fazer get")]
) -> LojaGET:

    loja_query_handler = QueryHandler(Loja, connection=connection)

    loja: Optional[Loja] = await loja_query_handler.find_one(uuid=uuid)
    if loja is None:
        raise NotFoundException('Loja não encontrada')

    response = await service.get_data(loja)
    return response


@router.get(
    "/"
)
async def requisitar_lojas(
    connection: dependencies.ConnectionDependency,
    service: dependencies.LojaServiceDependency,
    limit: int = Query(0),
    offset: int = Query(1),
) -> Lojas:

    loja_query_handler = QueryHandler(Loja, connection=connection)
    result: List[LojaGET] = []
    lojas: List[Loja] = await loja_query_handler.find_all()
    for loja in lojas:
        try:
            loja_data = await service.get_data(loja)
        except ValueError:  # endereço com defeito
            continue

        result.append(loja_data)

    paginate = Paginador(result, offset, limit)
    return Lojas(**paginate.get_response())


@router.post(
    "/login",
    tags=["Auth"],
    response_model=LojaAuthData
)
async def login(
    form_data: dependencies.Oauth2PasswordRequestFormDependency,
    auth_service: dependencies.AuthServiceDependency,
    service: dependencies.LojaServiceDependency,
) -> Any:

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
    service: dependencies.LojaServiceDependency,
    updated_data: LojaPUT,
    uuid: Annotated[str, Path(title="O uuid da loja a ser atualizada")]
):

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
async def signup(
    service: dependencies.LojaServiceDependency,
    loja: LojaSignUp
) -> Any:

    try:
        loja_cadastrada = await service.registrar(loja_data=loja)

    except InvalidPasswordException:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Senha inválida! A senha deve ser maior que 5"
        )

    except LojaJaCadastradaException:
        import traceback
        traceback.print_exc()
        raise ConflictException(detail="Credenciais inválidas!")

    except Exception as error:
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro no cadastro da loja! detail: {error}"
        )

    return {"uuid": loja_cadastrada.uuid}


@router.get("/produtos/")
async def requisitar_produtos_de_loja(
    loja: dependencies.CurrentLojaDependency,
    service: dependencies.LojaServiceDependency,
    limit: int = Query(0),
    offset: int = Query(1),
) -> Produtos:

    produtos = await service.get_all_produtos_from_loja(loja)
    paginate = Paginador(produtos, offset, limit)
    return Produtos(**paginate.get_response())


@router.post(
    '/imagem_cadastro',
    summary="Atualizar imagem de cadastro da loja",
    responses={
        404: {"description": "Loja não encontrada"}
    }
)
async def atualizar_imagem_de_cadastro(
    loja: dependencies.CurrentLojaDependency,
    image: LojaUpdateImageCadastro
) -> Dict[str, ImageUploadServiceResponse]:

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
    loja: dependencies.CurrentLojaDependency,
    image: LojaUpdateImageCadastro
):

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
    connection: dependencies.ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid da loja a ativar/inativar")],
    ativar: bool
) -> Any:

    loja_query_handler = QueryHandler(Loja, connection)
    cmd_handler = CommandHandler(connection)

    loja: Optional[Loja] = await loja_query_handler.find_one(uuid=uuid)
    if loja is None:
        raise NotFoundException('Loja não encontrada')

    cmd_handler.update(loja, {'ativo': ativar})
    await cmd_handler.commit()

    status_msg = "ativada" if ativar is True else "inativada"
    return {"message": f"Loja {status_msg} com sucesso!"}


@router.delete(
    "/{uuid}"
)
async def deletar_loja(
    connection: dependencies.ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid da loja a ser deletada")]
) -> Any:

    return {"message": "Loja deletada com sucesso!"}


@router.post("/cliente", status_code=status.HTTP_201_CREATED)
async def cadastrar_cliente(
    connection: dependencies.ConnectionDependency,
    loja: dependencies.CurrentLojaDependency,
    usuario: UsuarioFollowEmpresaRequest
) -> Any:

    if usuario.loja_uuid is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="uuid da loja em falta",
        )

    cliente = Cliente(
        usuario_uuid=usuario.usuario_uuid,
        loja_uuid=usuario.loja_uuid
    )

    cmd_handler = CommandHandler(connection)
    cmd_handler.save(cliente)

    results = await cmd_handler.commit()

    cliente_uuid = results[0].uuid

    return {"uuid": cliente_uuid}


@router.post("/cliente_v2/{loja_uuid}", status_code=status.HTTP_201_CREATED)
async def cadastrar_cliente_v2(
    connection: dependencies.ConnectionDependency,
    loja: dependencies.CurrentLojaDependency,
    user_service: dependencies.UserServiceDependency,
    usuario: UsuarioSignUp,
    loja_uuid: str
) -> Any:

    try:
        usuario_cadastrado = await user_service.registrar(
            user_data=usuario
        )
    except InvalidPasswordException:
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

    cmd_handler = CommandHandler(connection)

    cmd_handler.save(cliente)
    results = await cmd_handler.commit()
    cliente_uuid = results[0].uuid

    return {
        "usuario_uuid": usuario_cadastrado.uuid,
        "cliente_uuid": cliente_uuid
    }


@router.post('/refresh')
async def refresh(
    service: dependencies.LojaServiceDependency,
    loja: dependencies.CurrentLojaDependency,
    complete: str = Query('0')
):

    access_token = AuthService.create_access_token({"sub": loja.username})
    loja_data = None
    if complete == '1':
        loja_data = await service.get_data(loja)

    return LojaAuthData(
        access_token=access_token,
        token_type='bearer',
        loja=loja_data
    )


@router.get("/clientes/")
async def buscar_clientes(
    connection: dependencies.ConnectionDependency,
    loja: dependencies.CurrentLojaDependency,
) -> List[UsuarioGET]:

    response: List[UsuarioGET] = []

    cliente_query_handler = QueryHandler(Cliente, connection=connection)
    user_query_handler = QueryHandler(Usuario, connection=connection)
    endereco_query_handler = QueryHandler(
        EnderecoUsuario, connection=connection
    )

    clientes: List[Cliente]
    clientes = await cliente_query_handler.find_all(loja_uuid=loja.uuid)
    for cliente in clientes:
        cliente_usuario: Optional[Usuario]
        cliente_usuario = await user_query_handler.find_one(
            uuid=cliente.usuario_uuid
        )
        if cliente_usuario is None:
            continue

        del cliente_usuario.password
        del cliente_usuario.password_hash

        endereco = await endereco_query_handler.find_one(
            usuario_uuid=cliente_usuario.uuid
        )
        response_item = UsuarioGET(
            nome=cliente_usuario.nome,
            username=cliente_usuario.username,
            email=cliente_usuario.email,
            celular=cliente_usuario.celular,
            modo_de_cadastro=cliente_usuario.modo_de_cadastro,
            telefone=cliente_usuario.telefone,
            uuid=cliente_usuario.uuid
        )
        if endereco:
            response_item.endereco = endereco

        response.append(response_item)

    return response
