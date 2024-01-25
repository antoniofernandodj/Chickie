from typing import Annotated
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Request,
    Response,
    Query
)
from src.domain.models import AvaliacaoDeLoja
from src.infra.database_postgres.handlers import QueryHandler, CommandHandler
from src.misc import Paginador  # noqa
from src.dependencies import ConnectionDependency


router = APIRouter(prefix="/avaliacoes_loja", tags=["Avaliações de Lojas"])


@router.get("/")
async def requisitar_avaliacoes_loja(
    connection: ConnectionDependency,
    limit: int = Query(0),
    offset: int = Query(1),
):

    query_handler = QueryHandler(AvaliacaoDeLoja, connection=connection)
    results = await query_handler.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_avaliacao_loja(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid da avaliação fazer get")]
):

    query_handler = QueryHandler(AvaliacaoDeLoja, connection=connection)
    result = await query_handler.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("avaliacoes_lojanão encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_avaliacao_loja(
    connection: ConnectionDependency,
    avaliacao: AvaliacaoDeLoja,
):

    cmd_handler = CommandHandler(connection)
    try:
        cmd_handler.save(avaliacao)
        results = await cmd_handler.commit()
        uuid = results[0].uuid
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_avaliacao_loja_put(
    connection: ConnectionDependency,
    avaliacao_loja_data: AvaliacaoDeLoja,
    uuid: Annotated[str, Path(title="O uuid do avaliacoes_lojaa fazer put")],
):

    query_handler = QueryHandler(AvaliacaoDeLoja, connection=connection)
    cmd_handler = CommandHandler(connection)
    avaliacao = await query_handler.find_one(uuid=uuid)
    if avaliacao is None:
        raise NotFoundException("Avaliacao de Loja não encontrada")

    cmd_handler.update(
        avaliacao, avaliacao_loja_data.model_dump()  # type: ignore
    )
    await cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{uuid}")
async def atualizar_avaliacoes_loja_patch(
    connection: ConnectionDependency,
    avaliacoes_loja_data: AvaliacaoDeLoja,
    uuid: Annotated[str, Path(title="O uuid do avaliacoes_lojaa fazer patch")],
):

    query_handler = QueryHandler(AvaliacaoDeLoja, connection=connection)
    cmd_handler = CommandHandler(connection)
    avaliacao = await query_handler.find_one(uuid=uuid)
    if avaliacao is None:
        raise NotFoundException("Avaliação encontrada")

    cmd_handler.update(
        avaliacao, avaliacoes_loja_data.model_dump()  # type: ignore
    )
    await cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{uuid}")
async def remover_avaliacoes_loja(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid do avaliacoes_lojaa fazer delete")]
):

    cmd_handler = CommandHandler(connection)
    try:
        cmd_handler.delete_from_uuid(AvaliacaoDeLoja, uuid=uuid)
        await cmd_handler.commit()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return Response(status_code=status.HTTP_204_NO_CONTENT)
