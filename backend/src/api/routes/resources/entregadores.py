#
#
from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Depends,
    Query,
)
from typing import Optional
from src.api import security
from src.schemas import Loja, Entregador
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


current_company = Annotated[Loja, Depends(security.current_company)]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Entregador não encontrado"
)

router = APIRouter(prefix="/entregadores", tags=["Entregadores"])


@router.get("/")
async def requisitar_entregadores(loja_uuid: Optional[str] = Query(None)):
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Entregador, connection=connection)
        results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_entregador(
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer get")]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Entregador, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_entregadores(
    entregador: Entregador,
    current_company: current_company,
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Entregador, connection=connection)
        try:
            uuid = await repository.save(entregador)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_entregador_put(
    current_company: current_company,
    entregadorData: Entregador,
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer put")],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Entregador, connection=connection)
        entregador = await repository.find_one(uuid=uuid)
        if entregador is None:
            raise NotFoundException

        num_rows_affected = await repository.update(
            entregador, entregadorData.model_dump()  # type: ignore
        )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_entregador_patch(
    current_company: current_company,
    entregadorData: Entregador,
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer patch")],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Entregador, connection=connection)
        entregador = await repository.find_one(uuid=uuid)
        if entregador is None:
            raise NotFoundException

    num_rows_affected = await repository.update(
        entregador, entregadorData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_entregador(
    current_company: current_company,
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer delete")],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Entregador, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
