from typing import Annotated, Optional, Dict, List
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
from src.domain.models import CategoriaProdutos
from src.dependencies import (
    current_company,
)
from src.dependencies.connection_dependency import connection_dependency


router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"],
    # dependencies=[Depends(get_token_header)],
    # responses={
    #     404: {"description": "Categoria não encontrada"}
    # }
)


@router.get("/")
async def requisitar_categorias(
    connection: connection_dependency,
    nome: Optional[str] = Query(None),
    loja_uuid: Optional[str] = Query(None)
) -> List[CategoriaProdutos]:

    repository = Repository(CategoriaProdutos, connection)

    kwargs = {}
    if nome is not None:
        kwargs["nome"] = nome
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results: List[CategoriaProdutos] = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_categoria(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer get")],
    nome: Optional[str] = Query(None)
) -> CategoriaProdutos:

    repository = Repository(CategoriaProdutos, connection)

    kwargs = {}
    if nome is not None:
        kwargs["nome"] = nome

    result: Optional[CategoriaProdutos] = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Categoria não encontrada")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_categorias(
    categoria: CategoriaProdutos,
    connection: connection_dependency,
    current_company: current_company,
) -> Dict[str, str]:

    repository = Repository(CategoriaProdutos, connection)

    try:
        uuid = await repository.save(categoria)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.patch("/{uuid}")
async def atualizar_categoria_patch(
    current_company: current_company,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer patch")],
):
    return {}


@router.put("/{uuid}")
async def atualizar_categoria_put(
    connection: connection_dependency,
    current_company: current_company,
    itemData: CategoriaProdutos,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer put")],
) -> Dict[str, int]:

    repository = Repository(CategoriaProdutos, connection)

    try:
        categoria = await repository.find_one(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
    if categoria is None:
        raise NotFoundException("Categoria não encontrada")

    num_rows_affected = await repository.update(
        categoria, itemData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_categoria(
    connection: connection_dependency,
    current_company: current_company,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer delete")],
) -> Dict[str, int]:

    repository = Repository(CategoriaProdutos, connection)

    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
