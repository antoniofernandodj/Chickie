from typing import Annotated, Optional
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Depends,
    Query,
)
from src.api import security
from src.schemas import CategoriaProdutos, Loja
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


current_company = Annotated[Loja, Depends(security.current_company)]
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
async def requisitar_categorias(
    nome: Optional[str] = Query(None), loja_uuid: Optional[str] = Query(None)
):
    """
    Requisita todas as categorias de produtos ou filtra por nome e/ou UUID da loja.

    Args:
        nome (str, optional): Filtra as categorias pelo nome.
        loja_uuid (str, optional): Filtra as categorias pelo UUID da loja.

    Returns:
        List[CategoriaProdutos]: Uma lista contendo todas as categorias de produtos correspondentes aos filtros.
    """
    kwargs = {}
    if nome is not None:
        kwargs["nome"] = nome
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    async with DatabaseConnectionManager() as connection:
        repository = Repository(CategoriaProdutos, connection=connection)
        results = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_categoria(
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer get")]
):
    """
    Requisita uma categoria de produto específica com base no UUID.

    Args:
        uuid (str): O UUID da categoria.

    Returns:
        CategoriaProdutos: A categoria de produto correspondente ao UUID.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(CategoriaProdutos, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_categorias(
    categoria: CategoriaProdutos,
    current_company: current_company,
):
    """
    Cadastra uma nova categoria de produtos.

    Args:
        categoria (CategoriaProdutos): Os dados da categoria a ser cadastrada.
        current_company (Loja): A loja atual autenticada.

    Returns:
        dict: Um dicionário contendo o UUID da categoria cadastrada.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(CategoriaProdutos, connection=connection)
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
    current_company: current_company,
    itemData: CategoriaProdutos,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer put")],
):
    """
    Atualiza uma categoria de produtos utilizando o método PUT.

    Args:
        current_company (Loja): A loja atual autenticada.
        itemData (CategoriaProdutos): Os dados atualizados da categoria.
        uuid (str): O UUID da categoria a ser atualizada.

    Returns:
        dict: Um dicionário contendo o número de linhas afetadas pela atualização.
    """
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
    current_company: current_company,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer delete")],
):
    """
    Remove uma categoria de produtos com base no UUID.

    Args:
        current_company (Loja): A loja atual autenticada.
        uuid (str): O UUID da categoria a ser removida.

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(CategoriaProdutos, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
