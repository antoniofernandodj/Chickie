from typing import Annotated
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query
)
from typing import Optional
from src.schemas import Status
from src.dependencies import (
    status_repository_dependency,
    current_company
)


router = APIRouter(prefix="/status", tags=["Status"])


@router.get("/")
async def requisitar_varios_status(
    repository: status_repository_dependency,
    loja_uuid: Optional[str] = Query(None)
):
    """
    Requisita status cadastrados na plataforma.

    Args:
        loja_uuid (Optional[str]): O uuid da loja, caso necessário.

    Returns:
        list[Status]: Lista de status encontrados.
    """
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_status(
    repository: status_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do status a fazer get")]
):
    """
    Busca um status pelo seu uuid.

    Args:
        uuid (str): O uuid do status a ser buscado.

    Returns:
        Status: O status encontrado.

    Raises:
        HTTPException: Se o status não for encontrado.
    """
    result = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Status não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_status(
    status: Status,
    current_company: current_company,
    repository: status_repository_dependency
):
    """
    Cadastra um novo status na plataforma.

    Args:
        current_company: A empresa atual autenticada.
        status (Status): Os detalhes do status a ser cadastrado.

    Returns:
        dict: Um dicionário contendo o uuid do status cadastrado.

    Raises:
        HTTPException: Se ocorrer um erro durante o cadastro.
    """
    try:
        uuid = await repository.save(status)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_status_put(
    statusData: Status,
    current_company: current_company,
    repository: status_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do status a fazer put")],
):
    """
    Atualiza um status utilizando o método HTTP PUT.

    Args:
        current_company: A empresa atual autenticada.
        statusData (Status): Os novos dados do status.
        uuid (str): O uuid do status a ser atualizado.

    Returns:
        dict: Um dicionário contendo o número de
        linhas afetadas na atualização.

    Raises:
        HTTPException: Se o status não for encontrado.
    """
    status = await repository.find_one(uuid=uuid)
    if status is None:
        raise NotFoundException("Status não encontrado")

    num_rows_affected = await repository.update(
        status, statusData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_status_patch(
    statusData: Status,
    repository: status_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do Status a fazer patch")],
):
    return {}


@router.delete("/{uuid}")
async def remover_status(
    current_company: current_company,
    repository: status_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do status a fazer delete")]
):
    """
    Remove um status pelo seu uuid.

    Args:
        current_company: A empresa atual autenticada.
        uuid (str): O uuid do status a ser removido.

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
