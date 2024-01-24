from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Depends,
    Response
)
from src.api.security import oauth2_scheme
from typing import Optional
from src.domain.models import Entregador
from src.exceptions import NotFoundException
from src.api.security import AuthService
from src.infra.database_postgres.handlers import QueryHandler, CommandHandler
from src.misc import Paginador  # noqa
from src.dependencies import ConnectionDependency


router = APIRouter(prefix="/entregadores", tags=["Entregadores"])


@router.get("/")
async def requisitar_entregadores(
    connection: ConnectionDependency,
    loja_uuid: Optional[str] = Query(None),
    limit: int = Query(0),
    offset: int = Query(1),
):

    query_handler = QueryHandler(Entregador, connection=connection)
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results = await query_handler.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_entregador(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer get")]
):

    query_handler = QueryHandler(Entregador, connection=connection)
    result = await query_handler.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Entregador não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_entregadores(
    connection: ConnectionDependency,
    entregador: Entregador,
    token: Annotated[str, Depends(oauth2_scheme)],
):

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa

    command_handler = CommandHandler(Entregador, connection)
    try:
        command_handler.save(entregador)
        results = await command_handler.commit()
        uuid = results[0]
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_entregador_put(
    connection: ConnectionDependency,
    entregadorData: Entregador,
    token: Annotated[str, Depends(oauth2_scheme)],
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer put")],
):

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa
    query_handler = QueryHandler(Entregador, connection=connection)
    entregador = await query_handler.find_one(uuid=uuid)
    if entregador is None:
        raise NotFoundException("Entregador não encontrado")

    cmd_handler = CommandHandler(Entregador, connection)
    cmd_handler.update(
        entregador, entregadorData.model_dump()  # type: ignore
    )
    await cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{uuid}")
async def atualizar_entregador_patch(
    connection: ConnectionDependency,
    entregadorData: Entregador,
    token: Annotated[str, Depends(oauth2_scheme)],
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer patch")],
):

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa
    query_handler = QueryHandler(Entregador, connection=connection)

    cmd_handler = CommandHandler(Entregador, connection)
    entregador = await query_handler.find_one(uuid=uuid)
    if entregador is None:
        raise NotFoundException("Entregador não encontrado")

    cmd_handler.update(
        entregador, entregadorData.model_dump()  # type: ignore
    )
    await cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{uuid}")
async def remover_entregador(
    connection: ConnectionDependency,
    token: Annotated[str, Depends(oauth2_scheme)],
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer delete")],
):

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa

    cmd_handler = CommandHandler(Entregador, connection)
    try:
        cmd_handler.delete_from_uuid(uuid=uuid)
        await cmd_handler.commit()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return Response(status_code=status.HTTP_204_NO_CONTENT)
