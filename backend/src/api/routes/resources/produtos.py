from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Depends,
    Query,
)
from typing import Optional
from src.api import security
from src.schemas import Loja, Produto
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


current_company = Annotated[Loja, Depends(security.current_company)]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado"
)

router = APIRouter(prefix="/produtos", tags=["Produto"])


@router.get("/")
async def requisitar_produtos(loja_uuid: Optional[str] = Query(None)):
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
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Produto, connection=connection)
        results = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_produto(
    uuid: Annotated[str, Path(title="O uuid do produto a fazer get")]
):
    """
    Busca um produto pelo seu uuid.
    
    Args:
        uuid (str): O uuid do produto a ser buscado.
    
    Returns:
        Produto: O produto encontrado.
    
    Raises:
        HTTPException: Se o produto não for encontrado.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Produto, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_produtos(
    produto: Produto,
    current_company: current_company,
):
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
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Produto, connection=connection)
        try:
            uuid = await repository.save(produto)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_produto_put(
    produtoData: Produto,
    current_company: current_company,
    uuid: Annotated[str, Path(title="O uuid do produto a fazer put")],
):
    """
    Atualiza um produto utilizando o método HTTP PUT.
    
    Args:
        uuid (str): O uuid do produto a ser atualizado.
        produtoData (Produto): Os novos dados do produto.
        current_company: A empresa atual autenticada.
    
    Returns:
        dict: Um dicionário contendo o número de linhas afetadas na atualização.
    
    Raises:
        HTTPException: Se o produto não for encontrado.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Produto, connection=connection)
        produto = await repository.find_one(uuid=uuid)
        if produto is None:
            raise NotFoundException

        num_rows_affected = await repository.update(
            produto, produtoData.model_dump()  # type: ignore
        )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_produto_patch(
    produtoData: Produto,
    uuid: Annotated[str, Path(title="O uuid do produto a fazer patch")],
    current_company: current_company,
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Produto, connection=connection)
        produto = await repository.find_one(uuid=uuid)
        if produto is None:
            raise NotFoundException

        num_rows_affected = await repository.update(
            produto, produtoData.model_dump()  # type: ignore
        )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_produto(
    uuid: Annotated[str, Path(title="O uuid do produto a fazer delete")],
    current_company: current_company,
):
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
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Produto, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
