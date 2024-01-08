from typing import Annotated, Optional, List, Dict
from src.infra.database_postgres.repository import Repository
from src.exceptions import NotFoundException, ConflictException
from starlette import status
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query
)
from src.models import Preco
from src.dependencies import (
    current_company
)
from src.dependencies.connection_dependency import connection_dependency


router = APIRouter(prefix="/precos", tags=["Preços"])


@router.get("/")
async def requisitar_precos(
    connection: connection_dependency,
    produto_uuid: Optional[str] = Query(None)
) -> List[Preco]:
    """
    Obtém uma lista de todos os preços cadastrados.

    Args:
        produto_uuid (str, opcional): UUID da loja para filtrar os preços.

    Returns:
        list: Uma lista contendo os preços encontrados.
    """
    repository = Repository(Preco, connection)

    kwargs = {}
    if produto_uuid is not None:
        kwargs["produto_uuid"] = produto_uuid

    results: List[Preco] = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_preco(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do preco a fazer get")]
) -> Preco:
    """
    Obtém detalhes de um preço pelo seu UUID.

    Args:
        uuid (str): UUID do preço.

    Returns:
        Preco: Os detalhes do preço.
    """
    repository = Repository(Preco, connection)

    result: Optional[Preco] = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Preço não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_precos(
    preco: Preco,
    current_company: current_company,
    connection: connection_dependency,
) -> Dict[str, str]:
    """
    Cadastra um novo preço especial para um dado produto.

    Args:
        preco (Preco): Dados do preço a ser cadastrado.
        current_company (Loja): Dados da loja autenticada (dependência).

    Returns:
        dict: Um dicionário contendo o UUID do preço cadastrado.
    """
    repository = Repository(Preco, connection)

    query = await repository.find_one(
        dia_da_semana=preco.dia_da_semana,
        produto_uuid=preco.produto_uuid
    )
    if query:
        raise ConflictException('Preço já cadastrado para este '
                                'produto e para este dia da semana!')

    try:
        uuid = await repository.save(preco)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.patch("/{uuid}")
async def atualizar_preco_patch(
    current_company: current_company,
    uuid: Annotated[str, Path(title="O uuid do preco a fazer patch")]
):
    return {}


@router.put("/{uuid}")
async def atualizar_preco_put(
    itemData: Preco,
    current_company: current_company,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do preco a fazer put")]
) -> Dict[str, int]:
    """
    Atualiza um preço completamente usando PUT.

    Args:
        itemData (Preco): Dados do preço para atualização.
        uuid (str): UUID do preço a ser atualizado.
        current_company (Loja): Dados da loja autenticada (dependência).

    Returns:
        dict: Um dicionário contendo o número de linhas afetadas na
        atualização.
    """
    repository = Repository(Preco, connection)

    preco = await repository.find_one(uuid=uuid)
    if preco is None:
        raise NotFoundException("Preço não encontrado")

    num_rows_affected = await repository.update(
        preco, itemData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_preco(
    current_company: current_company,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do preco a fazer delete")]
) -> Dict[str, int]:
    """
    Remove um preço.

    Args:
        uuid (str): UUID do preço a ser removido.
        current_company (Loja): Dados da loja autenticada (dependência).

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    repository = Repository(Preco, connection)

    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
