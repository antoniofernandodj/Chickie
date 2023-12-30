from typing import Annotated, Optional, List, Dict
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
)
from src.schemas import Produto
from src.dependencies import (
    produto_repository_dependency,
    current_company
)


router = APIRouter(prefix="/produtos", tags=["Produto"])


@router.get("/")
async def requisitar_produtos(
    repository: produto_repository_dependency,
    loja_uuid: Optional[str] = Query(None),
    categoria_uuid: Optional[str] = Query(None)
) -> List[Produto]:

    """
    Requisita os produtos cadastrados na plataforma.
    Aceita um uuid como query para buscar os
    produtos de uma empresa específica

    Args:
        loja_uuid (Optional[str]): O uuid da empresa,
        caso necessário

    Returns:
        list[Produto]
    """
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid
    if categoria_uuid is not None:
        kwargs["categoria_uuid"] = categoria_uuid

    results: List[Produto] = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_produto(
    repository: produto_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do produto a fazer get")]
) -> Produto:

    """
    Busca um produto pelo seu uuid.

    Args:
        uuid (str): O uuid do produto a ser buscado.

    Returns:
        Produto: O produto encontrado.

    Raises:
        HTTPException: Se o produto não for encontrado.
    """
    produto: Optional[Produto] = await repository.find_one(uuid=uuid)
    if produto is None:
        raise NotFoundException("Produto não encontrado")

    return produto


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_produtos(
    repository: produto_repository_dependency,
    produto: Produto,
    current_company: current_company,
) -> Dict[str, str]:

    """
    Cadastra um novo produto na plataforma.

    Args:
        produto (Produto): Os detalhes do produto a ser cadastrado.
        current_company: A empresa atual autenticada.

    Returns:
        dict: Um dicionário contendo o uuid do produto cadastrado.

    Raises:
        HTTPException: Se ocorrer um erro durante o cadastro.
    """
    try:
        uuid = await repository.save(produto)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_produto_put(
    produtoData: Produto,
    current_company: current_company,
    repository: produto_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do produto a fazer put")]
) -> Dict[str, int]:

    """
    Atualiza um produto utilizando o método HTTP PUT.

    Args:
        uuid (str): O uuid do produto a ser atualizado.
        produtoData (Produto): Os novos dados do produto.
        current_company: A empresa atual autenticada.

    Returns:
        dict: Um dicionário contendo o número de linhas afetadas na
        atualização.

    Raises:
        HTTPException: Se o produto não for encontrado.
    """
    produto = await repository.find_one(uuid=uuid)
    if produto is None:
        raise NotFoundException("Produto não encontrado")

    num_rows_affected = await repository.update(
        produto, produtoData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_produto_patch(
    produtoData: Produto,
    current_company: current_company,
    repository: produto_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do produto a fazer patch")]
) -> Dict[str, int]:

    produto: Optional[Produto] = await repository.find_one(uuid=uuid)
    if produto is None:
        raise NotFoundException("Produto não encontrado")

    num_rows_affected = await repository.update(
        produto, produtoData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_produto(
    current_company: current_company,
    repository: produto_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do produto a fazer delete")]
) -> Dict[str, int]:
    """
    Remove um produto pelo seu uuid.

    Args:
        uuid (str): O uuid do produto a ser removido.
        current_company: A empresa atual autenticada.

    Returns:
        dict: Um dicionário contendo o número de itens removidos.

    Raises:
        HTTPException: Se ocorrer um erro durante a remoção.
    """
    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
