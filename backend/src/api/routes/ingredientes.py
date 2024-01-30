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
    Response,
    Response
)
from src.misc import Paginador  # noqa
from src.domain.models import Ingrediente
from src.infra.database_postgres.handlers import (
    QueryHandler, CommandHandler
)
from src.dependencies import ConnectionDependency, CurrentLojaDependency


router = APIRouter(prefix="/ingredientes", tags=["Ingrediente"])


@router.get("/")
async def requisitar_ingredientes(
    connection: ConnectionDependency,
    loja_uuid: Optional[str] = Query(None),
    produto_uuid: Optional[str] = Query(None)
) -> List[Ingrediente]:

    ingredientes_query_handler = QueryHandler(Ingrediente, connection)
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid
    if produto_uuid is not None:
        kwargs["produto_uuid"] = produto_uuid

    results: List[Ingrediente] = (
        await ingredientes_query_handler.find_all(**kwargs)
    )

    return results


@router.get("/{uuid}")
async def requisitar_ingrediente(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid do ingrediente a fazer get")]
) -> Ingrediente:

    ingredientes_query_handler = QueryHandler(Ingrediente, connection)
    result: Optional[Ingrediente] = (
        await ingredientes_query_handler.find_one(uuid=uuid)
    )
    if result is None:
        raise NotFoundException("Ingrediente não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_ingrediente(
    connection: ConnectionDependency,
    ingrediente: Ingrediente,
    loja: CurrentLojaDependency,
) -> Dict[str, str]:

    ingredientes_query_handler = QueryHandler(Ingrediente, connection)
    query = await ingredientes_query_handler.find_one(nome=ingrediente.nome)
    if query:
        raise ConflictException('Ingrediente Já cadastrado!')

    cmd_handler = CommandHandler(connection)

    try:
        cmd_handler.save(ingrediente)
        results = await cmd_handler.commit()
        uuid = results[0].uuid
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.delete("/{uuid}")
async def remover_ingrediente(
    connection: ConnectionDependency,
    loja: CurrentLojaDependency,
    uuid: Annotated[str, Path(title="O uuid do ingrediente a fazer delete")]
):

    cmd_handler = CommandHandler(connection)
    try:
        cmd_handler.delete_from_uuid(Ingrediente, uuid=uuid)
        await cmd_handler.commit()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return Response(status_code=status.HTTP_204_NO_CONTENT)
