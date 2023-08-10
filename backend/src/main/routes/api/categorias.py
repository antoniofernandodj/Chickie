from typing import Annotated, Optional
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Depends,
    Query,
)
from src.main import security
from src.schemas import CategoriaProdutos, Loja
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


current_user = Annotated[Loja, Depends(security.current_company)]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
)

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"],
    # dependencies=[Depends(get_token_header)],
    # responses={
    #     404: {"description": "Categoria não encontrada"}
    # }
)


@router.get("/")
async def requisitar_categorias(nome: Optional[str] = Query(None)):
    kwargs = {}
    if nome is not None:
        kwargs["nome"] = nome
    async with DatabaseConnectionManager() as connection:
        repository = Repository(CategoriaProdutos, connection=connection)
        results = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_categoria(
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer get")]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(CategoriaProdutos, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_categorias(
    categoria: CategoriaProdutos, current_user: current_user
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(CategoriaProdutos, connection=connection)
        try:
            uuid = await repository.save(categoria)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.patch("/{uuid}")
async def atualizar_categoria_patch(
    current_user: current_user,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer patch")],
):
    return {}


@router.put("/{uuid}")
async def atualizar_categoria_put(
    itemData: CategoriaProdutos,
    current_user: current_user,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer put")],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(CategoriaProdutos, connection=connection)
        try:
            categoria = await repository.find_one(uuid=uuid)
        except Exception as error:
            return {"error": str(error)}
        if categoria is None:
            raise NotFoundException

    num_rows_affected = await repository.update(
        categoria, itemData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_categoria(
    current_user: current_user,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer delete")],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(CategoriaProdutos, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
