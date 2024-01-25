from typing import Annotated, Optional, Dict, List
from src.exceptions import (
    NotFoundException,
    ConflictException
)
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Response
)
from src.misc import Paginador  # noqa
from src.domain.models import Adicional
from src.infra.database_postgres.handlers import QueryHandler, CommandHandler
from src.dependencies import ConnectionDependency, CurrentLojaDependency


router = APIRouter(prefix="/adicionais", tags=["Adicionais"])


@router.get("/")
async def requisitar_adicionais(
    connection: ConnectionDependency,
    loja_uuid: Optional[str] = Query(None)
) -> List[Adicional]:

    adicionais_query_handler = QueryHandler(Adicional, connection)
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results: List[Adicional] = (
        await adicionais_query_handler.find_all(**kwargs)
    )

    return results


@router.get("/{uuid}")
async def requisitar_adicional(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid do adicional a fazer get")]
) -> Adicional:

    adicional_query_handler = QueryHandler(Adicional, connection)
    result: Optional[Adicional] = await adicional_query_handler.find_one(
        uuid=uuid
    )
    if result is None:
        raise NotFoundException("Adicional não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_adicional(
    connection: ConnectionDependency,
    adicional: Adicional,
    loja: CurrentLojaDependency,
) -> Dict[str, str]:

    adicional_query_handler = QueryHandler(Adicional, connection)
    query = await adicional_query_handler.find_one(nome=adicional.nome)
    if query:
        raise ConflictException('Adicional Já cadastrado!')

    cmd_handler = CommandHandler(connection)

    try:
        cmd_handler.save(adicional)
        results = await cmd_handler.commit()
        uuid = results[0].uuid
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.delete("/{uuid}")
async def remover_adicional(
    connection: ConnectionDependency,
    loja: CurrentLojaDependency,
    uuid: Annotated[str, Path(title="O uuid do adicional a fazer delete")]
):

    cmd_handler = CommandHandler(connection)
    try:
        cmd_handler.delete_from_uuid(uuid=uuid, model=Adicional)
        await cmd_handler.commit()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return Response(status_code=status.HTTP_204_NO_CONTENT)
