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
from src.schemas import Loja, ZonaDeEntrega
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


current_user = Annotated[Loja, Depends(security.current_company)]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Zona de entrega não encontrada",
)

router = APIRouter(prefix="/zonas-de-entrega", tags=["Zonas de entrega"])


@router.get("/")
async def requisitar_zonas_de_entrega():
    async with DatabaseConnectionManager() as connection:
        repository = Repository(ZonaDeEntrega, connection=connection)
        results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_zona_de_entrega(
    uuid: Annotated[str, Path(title="O uuid da zona de entrega a fazer get")]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(ZonaDeEntrega, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_zonas_de_entrega(zona_de_entrega: ZonaDeEntrega):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(ZonaDeEntrega, connection=connection)
        try:
            uuid = await repository.save(zona_de_entrega)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_zona_de_entrega_put(
    zona_de_entrega_Data: ZonaDeEntrega,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer put")
    ],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(ZonaDeEntrega, connection=connection)
        zona_de_entrega = await repository.find_one(uuid=uuid)
        if zona_de_entrega is None:
            raise NotFoundException

    num_rows_affected = await repository.update(
        zona_de_entrega, zona_de_entrega_Data.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_zona_de_entrega_patch(
    zona_de_entregaData: ZonaDeEntrega,
    uuid: Annotated[
        str, Path(title="O uuid da zona de entrega a fazer patch")
    ],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(ZonaDeEntrega, connection=connection)
        zona_de_entrega = await repository.find_one(uuid=uuid)
        if zona_de_entrega is None:
            raise NotFoundException

    num_rows_affected = await repository.update(
        zona_de_entrega, zona_de_entregaData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_zona_de_entrega(
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer delete")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(ZonaDeEntrega, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
