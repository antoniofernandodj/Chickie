from typing import Annotated, List, Dict
from src.infra.database_postgres.repository import Repository
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Request
)
from typing import Optional
from src.domain.models import MetodoDePagamento
from src.dependencies import current_company
from src.dependencies.connection_dependency import connection_dependency


router = APIRouter(
    prefix="/metodos_de_pagamento", tags=["Métodos de pagamentos"]
)


@router.get("/")
async def requisitar_metodos_de_pagamento(
    request: Request,
    connection: connection_dependency,
    loja_uuid: Optional[str] = Query(None),
) -> List[MetodoDePagamento]:

    repository = Repository(MetodoDePagamento, connection=connection)

    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results: List[MetodoDePagamento] = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_metodo_de_pagamento(
    request: Request,
    connection: connection_dependency,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagamento a fazer get")
    ]
) -> MetodoDePagamento:

    repository = Repository(MetodoDePagamento, connection=connection)

    result: Optional[MetodoDePagamento] = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Metodo de pagamento não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_metodos_de_pagamento(
    request: Request,
    connection: connection_dependency,
    metodo_de_pagamento: MetodoDePagamento,
    current_company: current_company,
) -> Dict[str, str]:

    repository = Repository(MetodoDePagamento, connection=connection)

    try:
        uuid = await repository.save(metodo_de_pagamento)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_metodo_de_pagamento_put(
    request: Request,
    connection: connection_dependency,
    metodo_de_pagamento_data: MetodoDePagamento,
    current_company: current_company,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer put")
    ],
) -> Dict[str, int]:

    repository = Repository(MetodoDePagamento, connection=connection)

    metodo_de_pagamento: Optional[MetodoDePagamento] = await repository \
        .find_one(uuid=uuid)

    if metodo_de_pagamento is None:
        raise NotFoundException("Metodo de pagamento não encontrado")

    num_rows_affected = await repository.update(
        metodo_de_pagamento,
        metodo_de_pagamento_data.model_dump(),
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_metodo_de_pagamento_patch(
    request: Request,
    connection: connection_dependency,
    metodo_de_pagamentoData: MetodoDePagamento,
    current_company: current_company,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer patch")
    ],
) -> Dict[str, int]:
    repository = Repository(MetodoDePagamento, connection=connection)

    metodo_de_pagamento: Optional[MetodoDePagamento] = await repository \
        .find_one(uuid=uuid)

    if metodo_de_pagamento is None:
        raise NotFoundException("Metodo de pagamento não encontrado")

    num_rows_affected = await repository.update(
        metodo_de_pagamento,
        metodo_de_pagamentoData.model_dump(),  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_metodo_de_pagamento(
    request: Request,
    connection: connection_dependency,
    current_company: current_company,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer delete")
    ],
) -> Dict[str, int]:

    repository = Repository(MetodoDePagamento, connection=connection)

    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
