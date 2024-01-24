from typing import Annotated, List, Dict, Optional
from src.infra.database_postgres.handlers import QueryHandler, CommandHandler
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
from src.domain.models import Pagamento
from src.misc import Paginador  # noqa
from src.dependencies import ConnectionDependency


router = APIRouter(prefix="/pagamentos", tags=["Pagamentos"])


@router.get("/")
async def requisitar_pagamentos(
    connection: ConnectionDependency,
    loja_uuid: Optional[str] = Query(None),
    limit: int = Query(0),
    offset: int = Query(1),
) -> List[Pagamento]:

    query_handler = QueryHandler(Pagamento, connection=connection)
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results: List[Pagamento] = await query_handler.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_pagamento(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid do pagamento a fazer get")]
) -> Pagamento:

    query_handler = QueryHandler(Pagamento, connection=connection)
    result: Optional[Pagamento] = await query_handler.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Pagamento não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_pagamentos(
    connection: ConnectionDependency,
    pagamento: Pagamento
) -> Dict[str, str]:

    pagamentos_command_handler = CommandHandler(Pagamento, connection)
    try:
        pagamentos_command_handler.save(pagamento)
        results = await pagamentos_command_handler.commit()
        uuid = results[0].uuid
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_pagamento_put(
    connection: ConnectionDependency,
    pagamento_Data: Pagamento,
    uuid: Annotated[str, Path(title="O uuid do pagemento a fazer put")],
) -> Dict[str, int]:

    query_handler = QueryHandler(Pagamento, connection=connection)
    cmd_handler = CommandHandler(Pagamento, connection=connection)

    pagamento = await query_handler.find_one(uuid=uuid)
    if pagamento is None:
        raise NotFoundException("Pagamento não encontrado")

    cmd_handler.update(
        pagamento, pagamento_Data.model_dump()  # type: ignore
    )
    await cmd_handler.commit()

    return {}


@router.patch("/{uuid}")
async def atualizar_pagamento_patch(
    connection: ConnectionDependency,
    pagamentoData: Pagamento,
    uuid: Annotated[str, Path(title="O uuid do pagamento a fazer patch")],
) -> Dict[str, int]:

    query_handler = QueryHandler(Pagamento, connection=connection)
    cmd_handler = CommandHandler(Pagamento, connection=connection)
    pagamento = await query_handler.find_one(uuid=uuid)
    if pagamento is None:
        raise NotFoundException("Pagamento não encontrado")

    cmd_handler.update(
        pagamento, pagamentoData.model_dump()  # type: ignore
    )
    await cmd_handler.commit()

    return {}


@router.delete("/{uuid}")
async def remover_pagamento(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid do pagemento a fazer delete")]
) -> Dict[str, int]:

    cmd_handler = CommandHandler(Pagamento, connection=connection)
    try:
        cmd_handler.delete_from_uuid(uuid=uuid)
        await cmd_handler.commit()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {}
