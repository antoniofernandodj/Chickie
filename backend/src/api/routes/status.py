from typing import Annotated, Optional, Dict, List
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Request,
    Depends
)
from src.api.security import oauth2_scheme, AuthService
from src.misc import Paginador  # noqa
from aiopg import Connection
from src.domain.models import Status
from src.infra.database_postgres.repository import Repository
from src.dependencies import ConnectionDependency


router = APIRouter(prefix="/status", tags=["Status"])


@router.get("/")
async def requisitar_varios_status(
    request: Request,
    loja_uuid: Optional[str] = Query(None)
) -> List[Status]:

    connection: Connection = request.state.connection

    repository = Repository(Status, connection)
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results: List[Status] = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_status(
    request: Request,
    uuid: Annotated[str, Path(title="O uuid do status a fazer get")]
) -> Status:

    connection: Connection = request.state.connection

    repository = Repository(Status, connection)
    result: Optional[Status] = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Status não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_status(
    request: Request,
    status: Status,
    token: Annotated[str, Depends(oauth2_scheme)],
) -> Dict[str, str]:

    connection: Connection = request.state.connection
    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa
    repository = Repository(Status, connection)
    try:
        uuid = await repository.save(status)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_status_put(
    request: Request,
    statusData: Status,
    token: Annotated[str, Depends(oauth2_scheme)],
    uuid: Annotated[str, Path(title="O uuid do status a fazer put")],
) -> Dict[str, int]:

    connection: Connection = request.state.connection
    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa
    repository = Repository(Status, connection)
    status = await repository.find_one(uuid=uuid)
    if status is None:
        raise NotFoundException("Status não encontrado")

    num_rows_affected = await repository.update(
        status, statusData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_status_patch(
    request: Request,
    statusData: Status,
    uuid: Annotated[str, Path(title="O uuid do Status a fazer patch")],
) -> Dict:
    return {}


@router.delete("/{uuid}")
async def remover_status(
    request: Request,
    token: Annotated[str, Depends(oauth2_scheme)],
    uuid: Annotated[str, Path(title="O uuid do status a fazer delete")]
) -> Dict[str, int]:

    connection: Connection = request.state.connection
    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa
    repository = Repository(Status, connection)
    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
