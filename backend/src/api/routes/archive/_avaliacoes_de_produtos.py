from typing import Annotated, List, Dict, Optional
from src.infra.database_postgres.handlers import QueryHandler, CommandHandler
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Response,
    Query
)
from src.domain.models import AvaliacaoDeProduto
from src.misc import Paginador  # noqa
from src.dependencies import ConnectionDependency


router = APIRouter(
    prefix="/avaliacoes-de-produtos",
    tags=["Avaliações de produtos"]
)


@router.get("/")
async def requisitar_avaliacoes(
    connection: ConnectionDependency,
    limit: int = Query(0),
    offset: int = Query(1),
) -> List[AvaliacaoDeProduto]:

    query_handler = QueryHandler(AvaliacaoDeProduto, connection)
    results: List[AvaliacaoDeProduto] = await query_handler.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_avaliacao(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid da avaliação a fazer get")]
) -> AvaliacaoDeProduto:

    query_handler = QueryHandler(AvaliacaoDeProduto, connection)

    result: Optional[AvaliacaoDeProduto] = await query_handler.find_one(
        uuid=uuid
    )
    if result is None:
        raise NotFoundException("Avaliação não encontrada")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_avaliacoes(
    connection: ConnectionDependency,
    avaliacao: AvaliacaoDeProduto
) -> Dict[str, str]:

    cmd_handler = CommandHandler(connection)
    try:
        cmd_handler.save(avaliacao)
        results = await cmd_handler.commit()
        uuid = results[0].uuid
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_avaliacao_put(
    connection: ConnectionDependency,
    avaliacaoData: AvaliacaoDeProduto,
    uuid: Annotated[str, Path(title="O uuid da avaliação a fazer put")],
):

    query_handler = QueryHandler(AvaliacaoDeProduto, connection)
    avaliacao = await query_handler.find_one(uuid=uuid)
    if avaliacao is None:
        raise NotFoundException("Avaliação não encontrada")

    cmd_handler = CommandHandler(connection)
    cmd_handler.update(
        avaliacao, avaliacaoData.model_dump()  # type: ignore
    )
    await cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{uuid}")
async def atualizar_avaliacao_patch(
    connection: ConnectionDependency,
    avaliacaoData: AvaliacaoDeProduto,
    uuid: Annotated[str, Path(title="O uuid do avaliação a fazer patch")]
):

    query_handler = QueryHandler(AvaliacaoDeProduto, connection)
    avaliacao = await query_handler.find_one(uuid=uuid)
    if avaliacao is None:
        raise NotFoundException("Avaliação não encontrada")

    cmd_handler = CommandHandler(connection)
    cmd_handler.update(
        avaliacao,
        avaliacaoData.model_dump()  # type: ignore
    )
    await cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{uuid}")
async def remover_avaliacao(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid da avaliação a fazer delete")]
):

    cmd_handler = CommandHandler(connection)
    try:
        cmd_handler.delete_from_uuid(AvaliacaoDeProduto, uuid=uuid)
        await cmd_handler.commit()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return Response(status_code=status.HTTP_204_NO_CONTENT)
