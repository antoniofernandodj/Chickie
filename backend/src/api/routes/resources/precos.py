from typing import Annotated, Optional
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Depends,
    Query,
)
from src.api import security
from src.schemas import Preco, Loja
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


current_user = Annotated[Loja, Depends(security.current_company)]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Preço não encontrado"
)

router = APIRouter(prefix="/precos", tags=["Preços"])


@router.get("/")
async def requisitar_precos(loja_uuid: Optional[str] = Query(None)):
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Preco, connection=connection)
        results = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_preco(
    uuid: Annotated[str, Path(title="O uuid do preco a fazer get")]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Preco, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_precos(preco: Preco):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Preco, connection=connection)
        try:
            uuid = await repository.save(preco)
        except Exception as error:
            return {"error": str(error)}

    return {"uuid": uuid}


@router.patch("/{uuid}")
async def atualizar_preco_patch(
    uuid: Annotated[str, Path(title="O uuid do preco a fazer patch")]
):
    return {}


@router.put("/{uuid}")
async def atualizar_preco_put(
    itemData: Preco,
    uuid: Annotated[str, Path(title="O uuid do preco a fazer put")],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Preco, connection=connection)
        preco = await repository.find_one(uuid=uuid)
        if preco is None:
            raise NotFoundException

        num_rows_affected = await repository.update(
            preco, itemData.model_dump()  # type: ignore
        )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_preco(
    uuid: Annotated[str, Path(title="O uuid do preco a fazer delete")]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Preco, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
