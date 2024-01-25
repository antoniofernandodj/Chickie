from typing import Annotated, List, Dict, Optional
from src.infra.database_postgres.handlers import QueryHandler, CommandHandler
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Response,
    Depends
)
from src.api.security import oauth2_scheme, AuthService
from src.domain.models import MetodoDePagamento
from src.misc import Paginador  # noqa
from src.dependencies import ConnectionDependency


router = APIRouter(
    prefix="/metodos_de_pagamento", tags=["Métodos de pagamentos"]
)


@router.get("/")
async def requisitar_metodos_de_pagamento(
    connection: ConnectionDependency,
    loja_uuid: Optional[str] = Query(None),
    limit: int = Query(0),
    offset: int = Query(1),
) -> List[MetodoDePagamento]:

    query_handler = QueryHandler(MetodoDePagamento, connection=connection)
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results: List[MetodoDePagamento] = await query_handler.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_metodo_de_pagamento(
    connection: ConnectionDependency,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagamento a fazer get")
    ]
) -> MetodoDePagamento:

    query_handler = QueryHandler(MetodoDePagamento, connection=connection)
    result: Optional[MetodoDePagamento] = await query_handler.find_one(
        uuid=uuid
    )
    if result is None:
        raise NotFoundException("Metodo de pagamento não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_metodos_de_pagamento(
    connection: ConnectionDependency,
    metodo_de_pagamento: MetodoDePagamento,
    token: Annotated[str, Depends(oauth2_scheme)],
) -> Dict[str, str]:

    auth_service = AuthService(connection)

    loja = await auth_service.current_company(token)  # noqa
    query_handler = QueryHandler(MetodoDePagamento, connection=connection)
    query = await query_handler.find_one(nome=status.nome)
    if query:
        raise Exception

    cmd_handler = CommandHandler(connection)
    try:
        cmd_handler.save(metodo_de_pagamento)
        results = await cmd_handler.commit()
        uuid = results[0].uuid
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_metodo_de_pagamento_put(
    connection: ConnectionDependency,
    metodo_de_pagamento_data: MetodoDePagamento,
    token: Annotated[str, Depends(oauth2_scheme)],
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer put")
    ],
):

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa
    query_handler = QueryHandler(MetodoDePagamento, connection=connection)
    cmd_handler = CommandHandler(connection)

    metodo_de_pagamento: Optional[MetodoDePagamento] = (
        await query_handler.find_one(uuid=uuid)
    )

    if metodo_de_pagamento is None:
        raise NotFoundException("Metodo de pagamento não encontrado")

    cmd_handler.update(
        metodo_de_pagamento,
        metodo_de_pagamento_data.model_dump(),
    )
    await cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{uuid}")
async def atualizar_metodo_de_pagamento_patch(
    connection: ConnectionDependency,
    metodo_de_pagamentoData: MetodoDePagamento,
    token: Annotated[str, Depends(oauth2_scheme)],
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer patch")
    ],
):

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa
    query_handler = QueryHandler(MetodoDePagamento, connection=connection)
    cmd_handler = CommandHandler(connection)

    metodo_de_pagamento: Optional[MetodoDePagamento] = await query_handler \
        .find_one(uuid=uuid)

    if metodo_de_pagamento is None:
        raise NotFoundException("Metodo de pagamento não encontrado")

    cmd_handler.update(
        metodo_de_pagamento,
        metodo_de_pagamentoData.model_dump(),  # type: ignore
    )
    await cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{uuid}")
async def remover_metodo_de_pagamento(
    connection: ConnectionDependency,
    token: Annotated[str, Depends(oauth2_scheme)],
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer delete")
    ],
):

    auth_service = AuthService(connection)
    loja = await auth_service.current_company(token)  # noqa
    cmd_handler = CommandHandler(connection)
    try:
        cmd_handler.delete_from_uuid(MetodoDePagamento, uuid=uuid)
        await cmd_handler.commit()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return Response(status_code=status.HTTP_204_NO_CONTENT)
