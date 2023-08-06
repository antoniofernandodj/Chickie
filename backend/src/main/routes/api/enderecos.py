from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Depends,
    Query,
)
from src.schemas import Endereco
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


repo_name = "endereco"
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Endereço não encontrado"
)

router = APIRouter(prefix="/enderecos", tags=["Endereços"])


@router.get("/")
async def requisitar_enderecos():
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Endereco, connection=connection)
        results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_endereco(
    uuid: Annotated[str, Path(title="O uuid do endereço a fazer get")]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Endereco, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_enderecos(endereco: Endereco):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Endereco, connection=connection)
        try:
            uuid = await repository.save(endereco)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.patch("/{uuid}")
async def atualizar_endereco_patch(
    uuid: Annotated[str, Path(title="O uuid do endereço a fazer patch")]
):
    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_endereco_put(
    itemData: Endereco,
    uuid: Annotated[str, Path(title="O uuid do endereco a fazer put")],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Endereco, connection=connection)
        endereco = await repository.find_one(uuid=uuid)
        if endereco is None:
            raise NotFoundException

    num_rows_affected = await repository.update(
        endereco, itemData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_endereco(
    uuid: Annotated[str, Path(title="O uuid do endereço a fazer delete")]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Endereco, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
