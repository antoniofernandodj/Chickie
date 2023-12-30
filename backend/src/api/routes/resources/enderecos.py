from typing import Annotated, Optional, List, Dict
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path
)
from src.schemas import Endereco
from src.dependencies import (
    endereco_repository_dependency
)

router = APIRouter(prefix="/enderecos", tags=["Endereços"])


@router.get("/")
async def requisitar_enderecos(
    repository: endereco_repository_dependency
) -> List[Endereco]:
    """
    Requisita todos os endereços cadastrados.

    Returns:
        List[Endereco]: Uma lista contendo todos os endereços cadastrados.
    """
    results: List[Endereco] = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_endereco(
    repository: endereco_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do endereço a fazer get")]
) -> Endereco:
    """
    Requisita um endereço específico com base no UUID.

    Args:
        uuid (str): O UUID do endereço.

    Returns:
        Endereco: O endereço correspondente ao UUID.
    """
    result: Optional[Endereco] = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Endereço não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_enderecos(
    repository: endereco_repository_dependency,
    endereco: Endereco
):
    """
    Cadastra um novo endereço.

    Args:
        endereco (Endereco): Os dados do endereço a ser cadastrado.

    Returns:
        dict: Um dicionário contendo o UUID do endereço cadastrado.
    """
    try:
        uuid = await repository.save(endereco)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.patch("/{uuid}")
async def atualizar_endereco_patch(
    repository: endereco_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do endereço a fazer patch")]
) -> Dict[str, str]:

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_endereco_put(
    itemData: Endereco,
    repository: endereco_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do endereco a fazer put")],
) -> Dict[str, int]:
    
    """
    Atualiza um endereço utilizando o método PUT.

    Args:
        itemData (Endereco): Os dados atualizados do endereço.
        uuid (str): O UUID do endereço a ser atualizado.

    Returns:
        dict: Um dicionário contendo o número de linhas
        afetadas pela atualização.
    """
    endereco = await repository.find_one(uuid=uuid)
    if endereco is None:
        raise NotFoundException("Endereço não encontrado")

    num_rows_affected = await repository.update(
        endereco, itemData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_endereco(
    repository: endereco_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do endereço a fazer delete")]
) -> Dict[str, int]:

    """
    Remove um endereço com base no UUID.

    Args:
        uuid (str): O UUID do endereço a ser removido.

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
