from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Request
)
from typing import Optional
from src.domain.models import Entregador
from src.exceptions import NotFoundException
from src.infra.database_postgres.repository import Repository
from src.dependencies import (
    current_company
)

from src.dependencies.connection_dependency import connection_dependency


router = APIRouter(prefix="/entregadores", tags=["Entregadores"])


@router.get("/")
async def requisitar_entregadores(
    request: Request,
    connection: connection_dependency,
    loja_uuid: Optional[str] = Query(None)
):

    repository = Repository(Entregador, connection=connection)

    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_entregador(
    request: Request,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer get")]
):

    repository = Repository(Entregador, connection=connection)

    result = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Entregador não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_entregadores(
    request: Request,
    entregador: Entregador,
    current_company: current_company,
    connection: connection_dependency,
):

    repository = Repository(Entregador, connection=connection)

    try:
        uuid = await repository.save(entregador)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_entregador_put(
    request: Request,
    entregadorData: Entregador,
    current_company: current_company,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer put")],
):

    repository = Repository(Entregador, connection=connection)

    entregador = await repository.find_one(uuid=uuid)
    if entregador is None:
        raise NotFoundException("Entregador não encontrado")

    num_rows_affected = await repository.update(
        entregador, entregadorData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_entregador_patch(
    request: Request,
    entregadorData: Entregador,
    connection: connection_dependency,
    current_company: current_company,
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer patch")],
):
    repository = Repository(Entregador, connection=connection)

    entregador = await repository.find_one(uuid=uuid)
    if entregador is None:
        raise NotFoundException("Entregador não encontrado")

    num_rows_affected = await repository.update(
        entregador, entregadorData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_entregador(
    request: Request,
    current_company: current_company,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer delete")],
):

    repository = Repository(Entregador, connection=connection)

    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
