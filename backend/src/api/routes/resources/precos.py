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
from src.schemas import Preco, Loja
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


current_company = Annotated[Loja, Depends(security.current_company)]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Preço não encontrado"
)

router = APIRouter(prefix="/precos", tags=["Preços"])


@router.get("/")
async def requisitar_precos(loja_uuid: Optional[str] = Query(None)):
    """
    Obtém uma lista de todos os preços cadastrados.

    Args:
        loja_uuid (str, opcional): UUID da loja para filtrar os preços.

    Returns:
        list: Uma lista contendo os preços encontrados.
    """
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Preco, connection=connection)
        results = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_preco(
    uuid: Annotated[str, Path(title="O uuid do preco a fazer get")]
):
    """
    Obtém detalhes de um preço pelo seu UUID.

    Args:
        uuid (str): UUID do preço.

    Returns:
        Preco: Os detalhes do preço.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Preco, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_precos(
    preco: Preco,
    current_company: current_company,
):
    """
    Cadastra um novo preço.

    Args:
        preco (Preco): Dados do preço a ser cadastrado.
        current_company (Loja): Dados da loja autenticada (dependência).

    Returns:
        dict: Um dicionário contendo o UUID do preço cadastrado.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Preco, connection=connection)
        try:
            uuid = await repository.save(preco)
        except Exception as error:
            return {"error": str(error)}

    return {"uuid": uuid}


@router.patch("/{uuid}")
async def atualizar_preco_patch(
    uuid: Annotated[str, Path(title="O uuid do preco a fazer patch")],
    current_company: current_company,
):
    return {}


@router.put("/{uuid}")
async def atualizar_preco_put(
    itemData: Preco,
    uuid: Annotated[str, Path(title="O uuid do preco a fazer put")],
    current_company: current_company,
):
    """
    Atualiza um preço completamente usando PUT.

    Args:
        itemData (Preco): Dados do preço para atualização.
        uuid (str): UUID do preço a ser atualizado.
        current_company (Loja): Dados da loja autenticada (dependência).

    Returns:
        dict: Um dicionário contendo o número de linhas afetadas na atualização.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Preco, connection=connection)
        preco = await repository.find_one(uuid=uuid)
        if preco is None:
            raise NotFoundException

        num_rows_affected = await repository.update(
            preco, itemData.model_dump()  # type: ignore
        )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_preco(
    uuid: Annotated[str, Path(title="O uuid do preco a fazer delete")],
    current_company: current_company,
):
    """
    Remove um preço.

    Args:
        uuid (str): UUID do preço a ser removido.
        current_company (Loja): Dados da loja autenticada (dependência).

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Preco, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
