from typing import Any, Annotated, Optional
from src.exceptions import (
    UnauthorizedException,
    NotFoundException,
    InvalidPasswordException
)
from fastapi import (
    HTTPException,
    status,
    Response,
    Depends
)
from src.misc import Paginador  # noqa
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from src.infra.database_postgres.handlers import (
    QueryHandler, CommandHandler, CommandTypes
)
from src.api.security import AuthService, oauth2_scheme
from src.domain.models import (
    UsuarioFollowEmpresaRequest,
    UsuarioSignUp,
    EnderecoUsuario as Endereco,
    Usuario,
    Cliente,
    ClientePOST,
    UserAuthData,
)
from src.dependencies import ConnectionDependency, UserServiceDependency


router = APIRouter(prefix="/user", tags=["Usuario"])


@router.post("/login", response_model=UserAuthData, tags=["Auth"])
async def login_post(
    connection: ConnectionDependency,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Any:

    endereco_query_handler = QueryHandler(Endereco, connection=connection)
    auth_service = AuthService(connection)

    user = await auth_service.authenticate_user(
        form_data.username, form_data.password
    )

    if not user:
        raise UnauthorizedException("Credenciais Inválidas!")

    access_token = AuthService.create_access_token({"sub": user.username})
    endereco: Optional[Endereco] = await endereco_query_handler.find_one(
        usuario_uuid=user.uuid
    )

    response = {
        "access_token": access_token,
        "token_type": "bearer",
        "uuid": user.uuid,
        "nome": user.nome,
        "username": user.username,
        "email": user.email,
        "celular": user.celular
    }

    if endereco:
        response['endereco'] = endereco

    return response


@router.post("/signup", status_code=status.HTTP_201_CREATED, tags=["Auth"])
async def signup(
    connection: ConnectionDependency,
    service: UserServiceDependency,
    usuario: UsuarioSignUp
) -> Any:

    try:
        usuario_uuid = await service.registrar(user_data=usuario)
    except InvalidPasswordException:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Senha inválida! A senha deve ser maior que 5"
        )

    return {"uuid": usuario_uuid}


@router.put("/{uuid}")
async def update_user(
    connection: ConnectionDependency,
    uuid: str,
    user_data: UsuarioSignUp,
    token: Annotated[str, Depends(oauth2_scheme)],
    response: Response
) -> Any:
    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa

    endereco_query_handler = QueryHandler(Endereco, connection)
    endereco_command_handler = CommandHandler(Endereco, connection)

    user_query_handler = QueryHandler(Endereco, connection)
    user_command_handler = CommandHandler(Endereco, connection)

    usuario: Optional[Usuario] = await user_query_handler.find_one(uuid=uuid)
    if usuario is None or usuario.uuid is None:
        raise NotFoundException('Usuario não encontrado')

    def only_numbers(string: str | None) -> str | None:
        if string is None:
            return None

        return ''.join([n for n in string if n.isdecimal()])

    try:
        usuario_updated_data = dict(
            nome=user_data.nome,
            username=user_data.username,
            email=user_data.email,
            celular=only_numbers(user_data.celular),
            telefone=only_numbers(user_data.telefone),
            password_hash=usuario.password_hash,
        )

        user_command_handler.update(
            usuario, usuario_updated_data
        )

        await user_command_handler.commit()

        novo_endereco = Endereco(
            uf=user_data.uf,
            cidade=user_data.cidade,
            logradouro=user_data.logradouro,
            numero=user_data.numero,
            bairro=user_data.bairro,
            complemento=user_data.complemento,
            usuario_uuid=usuario.uuid
        )
        endereco: Optional[Endereco] = await endereco_query_handler.find_one(
            usuario_uuid=usuario.uuid
        )
        if endereco:
            endereco_command_handler.delete(endereco)

        endereco_command_handler.save(novo_endereco)

        endereco_uuid: Optional[str] = None
        results = await endereco_command_handler.commit()
        for result in results:
            if result.command_type == CommandTypes.save:
                endereco_uuid = result.uuid

        if endereco_uuid is None:
            message = (
                "Usuario atualizado com sucesso, mas houve erro "
                "na atualização do endereço"
            )

        else:
            message = "Usuario atualizado com sucesso!"

        return {
            "message": message,
            "uuid": usuario.uuid,
            'endereco_uuid': endereco_uuid
        }

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao atualizar dados de usuario! Detalhes: {error}"
        )


@router.post("/seguir-loja")
async def seguir_loja(
    connection: ConnectionDependency,
    response: Response,
    token: Annotated[str, Depends(oauth2_scheme)],
    follow_request_data: UsuarioFollowEmpresaRequest
) -> Any:
    result: str | int
    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa
    cliente = ClientePOST(
        usuario_uuid=follow_request_data.usuario_uuid,
        loja_uuid=follow_request_data.loja_uuid
    )

    cliente_query_handler = QueryHandler(Cliente, connection=connection)
    cliente_cmd_handler = CommandHandler(Cliente, connection)

    if follow_request_data.follow:
        response.status_code = 201

        cliente_cmd_handler.save(cliente)
        results = await cliente_cmd_handler.commit()
        result = results[0].uuid
        return {"result": result, 'follow': follow_request_data.follow}

    else:
        relationship: Optional[Cliente] = await cliente_query_handler.find_one(
            usuario_uuid=follow_request_data.usuario_uuid,
            loja_uuid=follow_request_data.loja_uuid
        )

        if relationship:
            cliente_cmd_handler.delete(relationship)
            await cliente_cmd_handler.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/segue-loja/{uuid}")
async def segue_loja(
    connection: ConnectionDependency,
    token: Annotated[str, Depends(oauth2_scheme)],
    uuid: str
) -> Any:

    auth_service = AuthService(connection)
    current_user = await auth_service.current_user(token)
    if current_user.uuid is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Usuario sem uuid'
        )

    cliente_query_handler = QueryHandler(Cliente, connection=connection)
    follows: Optional[Cliente] = await cliente_query_handler.find_one(
        usuario_uuid=current_user.uuid,
        loja_uuid=uuid
    )
    if follows:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
