from typing import Annotated, Optional, Dict, List
from src.infra.database_postgres.repository import QueryHandler, CommandHandler
from src.exceptions import (
    NotFoundException,
    ConflictException,
)
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Request,
    Depends,
    Response
)
from src.domain.models import CategoriaProdutos, CategoriasProdutos
from src.misc import Paginador  # noqa
from src.dependencies import ConnectionDependency, CurrentLojaDependency


router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.get("/")
async def requisitar_categorias(
    connection: ConnectionDependency,
    nome: Optional[str] = Query(None),
    loja_uuid: Optional[str] = Query(None),
    limit: int = Query(0),
    offset: int = Query(1),
) -> CategoriasProdutos:

    categorias_query_handler = QueryHandler(CategoriaProdutos, connection)

    kwargs = {}
    if nome is not None:
        kwargs["nome"] = nome
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results: List[CategoriaProdutos] = (
        await categorias_query_handler.find_all(**kwargs)
    )
    paginate = Paginador(results, offset, limit)

    return CategoriasProdutos(**paginate.get_response())


@router.get("/{uuid}")
async def requisitar_categoria(
    connection: ConnectionDependency,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer get")],
    nome: Optional[str] = Query(None)
) -> CategoriaProdutos:

    categorias_query_handler = QueryHandler(CategoriaProdutos, connection)
    kwargs = {}
    if nome is not None:
        kwargs["nome"] = nome

    result: Optional[CategoriaProdutos] = (
        await categorias_query_handler.find_one(uuid=uuid)
    )
    if result is None:
        raise NotFoundException("Categoria não encontrada")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_categorias(
    connection: ConnectionDependency,
    categoria: CategoriaProdutos,
    loja: CurrentLojaDependency,
) -> Dict[str, str]:

    categorias_query_handler = QueryHandler(CategoriaProdutos, connection)
    query = await categorias_query_handler.find_one(nome=categoria.nome)
    if query:
        raise ConflictException('Categoria já cadastrada!')

    command_handler = CommandHandler(CategoriaProdutos, connection)
    try:
        command_handler.save(categoria)
        results = await command_handler.commit()
        uuid = results[0].uuid
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.patch("/{uuid}")
async def atualizar_categoria_patch(
    connection: ConnectionDependency,
    loja: CurrentLojaDependency,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer patch")],
):

    return {}


@router.put("/{uuid}")
async def atualizar_categoria_put(
    connection: ConnectionDependency,
    loja: CurrentLojaDependency,
    itemData: CategoriaProdutos,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer put")],
):

    categorias_query_handler = QueryHandler(CategoriaProdutos, connection)
    categorias_cmd_handler = CommandHandler(CategoriaProdutos, connection)
    try:
        categoria = await categorias_query_handler.find_one(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
    if categoria is None:
        raise NotFoundException("Categoria não encontrada")

    categorias_cmd_handler.update(
        categoria, itemData.model_dump()  # type: ignore
    )
    await categorias_cmd_handler.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{uuid}")
async def remover_categoria(
    connection: ConnectionDependency,
    loja: CurrentLojaDependency,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer delete")],
):

    categorias_cmd_handler = CommandHandler(CategoriaProdutos, connection)

    try:
        categorias_cmd_handler.delete_from_uuid(uuid=uuid)
        await categorias_cmd_handler.commit()
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return Response(status_code=status.HTTP_204_NO_CONTENT)
