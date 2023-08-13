from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Depends,
    Query,
)
from src.api import security
from typing import Optional
from src.schemas import Loja, Status
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


current_user = Annotated[Loja, Depends(security.current_company)]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Status não encontrado"
)

router = APIRouter(prefix="/status", tags=["Status"])


@router.get("/")
async def requisitar_um_status(loja_uuid: Optional[str] = Query(None)):
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Status, connection=connection)
        results = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_muitos_status(
    uuid: Annotated[str, Path(title="O uuid do status a fazer get")]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Status, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_Statuss(status: Status):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Status, connection=connection)
        try:
            uuid = await repository.save(status)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_status_put(
    statusData: Status,
    uuid: Annotated[str, Path(title="O uuid do status a fazer put")],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Status, connection=connection)
        status = await repository.find_one(uuid=uuid)
        if status is None:
            raise NotFoundException

    num_rows_affected = await repository.update(
        status, statusData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_status_patch(
    statusData: Status,
    uuid: Annotated[str, Path(title="O uuid do Status a fazer patch")],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Status, connection=connection)
        status = await repository.find_one(uuid=uuid)
        if status is None:
            raise NotFoundException

        num_rows_affected = await repository.update(
            status, statusData.model_dump()  # type: ignore
        )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_status(
    uuid: Annotated[str, Path(title="O uuid do status a fazer delete")]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Status, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
