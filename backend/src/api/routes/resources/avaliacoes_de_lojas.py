from typing import Annotated
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path
)
from src.models import AvaliacaoDeLoja
from src.infra.database_postgres.repository import Repository
from src.dependencies.connection_dependency import (
    connection_dependency
)


router = APIRouter(prefix="/avaliacoes_loja", tags=["Avaliações de Lojas"])


@router.get("/")
async def requisitar_avaliacoes_loja(connection: connection_dependency):
    """
    Requisita todas as avaliações de loja cadastradas.

    Returns:
        List[AvaliacaoDeLoja]: Uma lista contendo todos as avaliações de loja cadastradas.  # noqa
    """
    repository = Repository(AvaliacaoDeLoja, connection=connection)
    results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_avaliacao_loja(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid da avaliação fazer get")]
):
    """
    Requisita uma avaliação de loja específica com base no UUID.

    Args:
        uuid (str): O UUID da avaliação de loja

    Returns:
        avaliacao_loja (AvaliacaoDeLoja): A avaliação de loja correspondente ao UUID.  # noqa
    """
    repository = Repository(AvaliacaoDeLoja, connection=connection)
    result = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("avaliacoes_lojanão encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_avaliacao_loja(
    connection: connection_dependency,
    avaliacao: AvaliacaoDeLoja,
):
    """
    Cadastra uma nova avaliação de loja

    Args:
        avaliacoes_loja: Os dados da avaliação a ser cadastrada.

    Returns:
        dict: Um dicionário contendo o UUID da avaliação cadastrada.
    """
    repository = Repository(AvaliacaoDeLoja, connection=connection)
    try:
        uuid = await repository.save(avaliacao)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_avaliacao_loja_put(
    avaliacao_loja_data: AvaliacaoDeLoja,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do avaliacoes_lojaa fazer put")],
):
    """
    Atualiza um avaliacoes_lojautilizando o método PUT.

    Args:
        avaliacao_loja_data: Os dados atualizados da Avaliação
        uuid (str): O UUID da avaliação ser atualizada.

    Returns:
        dict: Um dicionário contendo o número de linhas afetadas pela atualização. # noqa
    """
    repository = Repository(AvaliacaoDeLoja, connection=connection)
    avaliacao = await repository.find_one(uuid=uuid)
    if avaliacao is None:
        raise NotFoundException("Avaliacao de Loja não encontrada")

    num_rows_affected = await repository.update(
        avaliacao, avaliacao_loja_data.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_avaliacoes_loja_patch(
    avaliacoes_loja_data: AvaliacaoDeLoja,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do avaliacoes_lojaa fazer patch")],
):
    repository = Repository(AvaliacaoDeLoja, connection=connection)
    avaliacao = await repository.find_one(uuid=uuid)
    if avaliacao is None:
        raise NotFoundException("Avaliação encontrada")

    num_rows_affected = await repository.update(
        avaliacao, avaliacoes_loja_data.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_avaliacoes_loja(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do avaliacoes_lojaa fazer delete")]
):
    """
    Remove um avaliacoes_lojacom base no UUID.

    Args:
        uuid (str): O UUID do avaliacoes_lojaa ser removido.

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    repository = Repository(AvaliacaoDeLoja, connection=connection)
    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
