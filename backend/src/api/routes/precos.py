from typing import Annotated, Optional, List, Dict
from src.infra.database_postgres.handlers import QueryHandler, CommandHandler
from src.exceptions import (
    NotFoundException,
    ConflictException,
)
from starlette import status
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Response
)
from src.domain.models import Preco
from src.misc import Paginador  # noqa
from src.dependencies import ConnectionDependency, LojaServiceDependency


router = APIRouter(prefix="/precos", tags=["Preços"])


@router.get("/")
async def requisitar_precos(
    connection: ConnectionDependency,
    produto_uuid: Optional[str] = Query(None),
    limit: int = Query(0),
    offset: int = Query(1),
) -> List[Preco]:

    query_handler = QueryHandler(Preco, connection)
    kwargs = {}
    if produto_uuid is not None:
        kwargs["produto_uuid"] = produto_uuid

    results: List[Preco] = await query_handler.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_preco(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid do preco a fazer get")]
) -> Preco:

    query_handler = QueryHandler(Preco, connection)
    result: Optional[Preco] = await query_handler.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Preço não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_precos(
    connection: ConnectionDependency,
    preco: Preco,
    loja: LojaServiceDependency,
) -> Dict[str, str]:

    query_handler = QueryHandler(Preco, connection)
    command_handler = CommandHandler(Preco, connection)

    query = await query_handler.find_one(
        dia_da_semana=preco.dia_da_semana,
        produto_uuid=preco.produto_uuid
    )
    if query:
        raise ConflictException('Preço já cadastrado para este '
                                'produto e para este dia da semana!')
    try:
        command_handler.save(preco)
        results = await command_handler.commit()
        uuid = results[0].uuid
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.patch("/{uuid}")
async def atualizar_preco_patch(
    connection: ConnectionDependency,
    loja: LojaServiceDependency,
    uuid: Annotated[str, Path(title="O uuid do preco a fazer patch")]
):

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{uuid}")
async def atualizar_preco_put(
    connection: ConnectionDependency,
    itemData: Preco,
    loja: LojaServiceDependency,
    uuid: Annotated[str, Path(title="O uuid do preco a fazer put")]
):

    preco_query_handler = QueryHandler(Preco, connection)
    preco_cmd_handler = CommandHandler(Preco, connection)
    preco = await preco_query_handler.find_one(uuid=uuid)
    if preco is None:
        raise NotFoundException("Preço não encontrado")

    preco_cmd_handler.update(preco, itemData.model_dump())
    await preco_cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{uuid}")
async def remover_preco(
    connection: ConnectionDependency,
    loja: LojaServiceDependency,
    uuid: Annotated[str, Path(title="O uuid do preco a fazer delete")]
):

    preco_cmd_handler = CommandHandler(Preco, connection)
    try:
        preco_cmd_handler.delete_from_uuid(uuid=uuid)
        await preco_cmd_handler.commit()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return Response(status_code=status.HTTP_204_NO_CONTENT)
