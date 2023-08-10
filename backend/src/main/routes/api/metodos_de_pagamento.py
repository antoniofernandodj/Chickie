from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Depends,
    Query,
)
from src.main import security
from src.schemas import Loja, MetodoDePagamento
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


current_user = Annotated[Loja, Depends(security.current_company)]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Metodo de pagamento não encontrado",
)

router = APIRouter(
    prefix="/metodos_de_pagamento", tags=["Métodos de pagamentos"]
)


@router.get("/")
async def requisitar_metodos_de_pagamento():
    async with DatabaseConnectionManager() as connection:
        repository = Repository(MetodoDePagamento, connection=connection)
        results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_metodo_de_pagamento(
    uuid: Annotated[
        str, Path(title="O uuid do método de pagamento a fazer get")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(MetodoDePagamento, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_metodos_de_pagamento(
    metodo_de_pagamento: MetodoDePagamento,
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(MetodoDePagamento, connection=connection)
        try:
            uuid = await repository.save(metodo_de_pagamento)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_metodo_de_pagamento_put(
    metodo_de_pagamento_Data: MetodoDePagamento,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer put")
    ],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(MetodoDePagamento, connection=connection)
        metodo_de_pagamento = await repository.find_one(uuid=uuid)
        if metodo_de_pagamento is None:
            raise NotFoundException

    num_rows_affected = await repository.update(
        metodo_de_pagamento,
        metodo_de_pagamento_Data.model_dump(),  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_metodo_de_pagamento_patch(
    metodo_de_pagamentoData: MetodoDePagamento,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer patch")
    ],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(MetodoDePagamento, connection=connection)
        metodo_de_pagamento = await repository.find_one(uuid=uuid)
        if metodo_de_pagamento is None:
            raise NotFoundException

    num_rows_affected = await repository.update(
        metodo_de_pagamento,
        metodo_de_pagamentoData.model_dump(),  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_metodo_de_pagamento(
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer delete")
    ]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(MetodoDePagamento, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
