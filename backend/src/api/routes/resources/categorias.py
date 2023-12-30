from typing import Annotated, Optional, Dict, List
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
)
from src.schemas import CategoriaProdutos
from src.dependencies import (
    current_company,
    categoria_repository_dependency
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
    repository: categoria_repository_dependency,
    nome: Optional[str] = Query(None),
    loja_uuid: Optional[str] = Query(None)
) -> List[CategoriaProdutos]:

    """
    Requisita todas as categorias de produtos ou filtra por
    nome e/ou UUID da loja.

    Args:
        nome (str, optional): Filtra as categorias pelo nome.
        loja_uuid (str, optional): Filtra as categorias pelo UUID da loja.

    Returns:
        List[CategoriaProdutos]: Uma lista contendo todas as
        categorias de produtos correspondentes aos filtros.
    """
    kwargs = {}
    if nome is not None:
        kwargs["nome"] = nome
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results: List[CategoriaProdutos] = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_categoria(
    repository: categoria_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer get")],
    nome: Optional[str] = Query(None)
) -> CategoriaProdutos:

    """
    Requisita uma categoria de produto específica com base no UUID.

    Args:
        uuid (str): O UUID da categoria.

    Returns:
        CategoriaProdutos: A categoria de produto correspondente ao UUID.
    """
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
    repository: categoria_repository_dependency,
    current_company: current_company,
) -> Dict[str, str]:

    """
    Cadastra uma nova categoria de produtos.

    Args:
        categoria (CategoriaProdutos): Os dados da categoria a ser cadastrada.
        current_company (Loja): A loja atual autenticada.

    Returns:
        dict: Um dicionário contendo o UUID da categoria cadastrada.
    """
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
    repository: categoria_repository_dependency,
    current_company: current_company,
    itemData: CategoriaProdutos,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer put")],
) -> Dict[str, int]:

    """
    Atualiza uma categoria de produtos utilizando o método PUT.

    Args:
        current_company (Loja): A loja atual autenticada.
        itemData (CategoriaProdutos): Os dados atualizados da categoria.
        uuid (str): O UUID da categoria a ser atualizada.

    Returns:
        dict: Um dicionário contendo o número de linhas
        afetadas pela atualização.
    """
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
    repository: categoria_repository_dependency,
    current_company: current_company,
    uuid: Annotated[str, Path(title="O uuid da categoria a fazer delete")],
) -> Dict[str, int]:
    """
    Remove uma categoria de produtos com base no UUID.

    Args:
        current_company (Loja): A loja atual autenticada.
        uuid (str): O UUID da categoria a ser removida.

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
