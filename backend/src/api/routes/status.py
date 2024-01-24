from typing import Annotated, Optional, Dict, List
from src.exceptions import (
    NotFoundException,
    ConflictException
)
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Response,
    Response
)
from src.misc import Paginador  # noqa
from src.domain.models import Status
from src.infra.database_postgres.handlers import QueryHandler, CommandHandler
from src.dependencies import ConnectionDependency, CurrentLojaDependency


router = APIRouter(prefix="/status", tags=["Status"])


@router.get("/")
async def requisitar_varios_status(
    connection: ConnectionDependency,
    loja_uuid: Optional[str] = Query(None)
) -> List[Status]:

    status_query_handler = QueryHandler(Status, connection)
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results: List[Status] = await status_query_handler.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_status(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid do status a fazer get")]
) -> Status:

    status_query_handler = QueryHandler(Status, connection)
    result: Optional[Status] = await status_query_handler.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Status não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_status(
    connection: ConnectionDependency,
    status: Status,
    loja: CurrentLojaDependency,
) -> Dict[str, str]:

    status_query_handler = QueryHandler(Status, connection)
    query = await status_query_handler.find_one(nome=status.nome)
    if query:
        raise ConflictException('Status Já cadastrado!')

    command_handler = CommandHandler(Status, connection)

    try:
        command_handler.save(status)
        results = await command_handler.commit()
        uuid = results[0].uuid
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_status_put(
    connection: ConnectionDependency,
    status_data: Status,
    loja: CurrentLojaDependency,
    uuid: Annotated[str, Path(title="O uuid do status a fazer put")],
):

    status_query_handler = QueryHandler(Status, connection)
    status_command_handler = CommandHandler(Status, connection)
    status_item = await status_query_handler.find_one(uuid=uuid)
    if status_item is None:
        raise NotFoundException("Status não encontrado")

    status_command_handler.update(
        status_item, status_data.model_dump()  # type: ignore
    )
    await status_command_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{uuid}")
async def atualizar_status_patch(
    connection: ConnectionDependency,
    statusData: Status,
    uuid: Annotated[str, Path(title="O uuid do Status a fazer patch")],
):
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{uuid}")
async def remover_status(
    connection: ConnectionDependency,
    loja: CurrentLojaDependency,
    uuid: Annotated[str, Path(title="O uuid do status a fazer delete")]
):

    status_cmd_handler = CommandHandler(Status, connection)
    try:
        status_cmd_handler.delete_from_uuid(uuid=uuid)
        await status_cmd_handler.commit()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return Response(status_code=status.HTTP_204_NO_CONTENT)
