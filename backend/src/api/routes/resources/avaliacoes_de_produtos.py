from typing import Annotated, List, Dict, Optional
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path
)
from src.schemas import AvaliacaoDeProduto
from src.dependencies import (
    connection_dependency,
    avaliacao_repository_dependency
)

router = APIRouter(
    prefix="/avaliacoes-de-produtos",
    tags=["Avaliações de produtos"]
)


@router.get("/")
async def requisitar_avaliacoes(
    repository: avaliacao_repository_dependency,
    connection: connection_dependency
) -> List[AvaliacaoDeProduto]:

    """
    Requisita todas as avaliações de produtos.

    Returns:
        List[AvaliacaoDeProduto]: Uma lista contendo todas
        as avaliações de produtos.
    """
    results: List[AvaliacaoDeProduto] = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_avaliacao(
    repository: avaliacao_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid da avaliação a fazer get")]
) -> AvaliacaoDeProduto:

    """
    Requisita uma avaliação de produto específica com base no UUID.

    Args:
        uuid (str): O UUID da avaliação.

    Returns:
        AvaliacaoDeProduto: A avaliação de produto correspondente ao UUID.
    """
    result: Optional[AvaliacaoDeProduto] = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Avaliação não encontrada")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_avaliacoes(
    repository: avaliacao_repository_dependency,
    avaliacao: AvaliacaoDeProduto
) -> Dict[str, str]:

    """
    Cadastra uma nova avaliação de produto.

    Args:
        avaliacao (AvaliacaoDeProduto): Os dados da avaliação a ser cadastrada.

    Returns:
        dict: Um dicionário contendo o UUID da avaliação cadastrada.
    """
    try:
        uuid = await repository.save(avaliacao)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_avaliacao_put(
    repository: avaliacao_repository_dependency,
    avaliacaoData: AvaliacaoDeProduto,
    uuid: Annotated[str, Path(title="O uuid da avaliação a fazer put")],
) -> Dict[str, int]:

    """
    Atualiza uma avaliação de produto utilizando o método PUT.

    Args:
        avaliacaoData (AvaliacaoDeProduto): Os dados atualizados da avaliação.
        uuid (str): O UUID da avaliação a ser atualizada.

    Returns:
        dict: Um dicionário contendo o número de linhas
        afetadas pela atualização.
    """
    avaliacao = await repository.find_one(uuid=uuid)
    if avaliacao is None:
        raise NotFoundException("Avaliação não encontrada")

    num_rows_affected = await repository.update(
        avaliacao, avaliacaoData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_avaliacao_patch(
    avaliacaoData: AvaliacaoDeProduto,
    repository: avaliacao_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do avaliação a fazer patch")]
) -> Dict[str, int]:

    avaliacao = await repository.find_one(uuid=uuid)
    if avaliacao is None:
        raise NotFoundException("Avaliação não encontrada")

    num_rows_affected = await repository.update(
        avaliacao,
        avaliacaoData.model_dump()  # type: ignore
    )

    return {'num_rows_affected': num_rows_affected}


@router.delete("/{uuid}")
async def remover_avaliacao(
    repository: avaliacao_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid da avaliação a fazer delete")]
) -> Dict[str, int]:

    """
    Remove uma avaliação de produto com base no UUID.

    Args:
        uuid (str): O UUID da avaliação a ser removida.e

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
