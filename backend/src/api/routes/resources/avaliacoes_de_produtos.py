from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path
)
from src.schemas import AvaliacaoDeProduto
from src.infra.database_postgres.repository import Repository
from src.dependencies import (
    connection_dependency
)

router = APIRouter(
    prefix="/avaliacoes-de-produtos",
    tags=["Avaliações de produtos"]
)

NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Avaliação não encontrada"
)

@router.get("/")
async def requisitar_avaliacoes(connection: connection_dependency):
    """
    Requisita todas as avaliações de produtos.

    Returns:
        List[AvaliacaoDeProduto]: Uma lista contendo todas as avaliações de produtos.
    """
    repository = Repository(AvaliacaoDeProduto, connection=connection)
    results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_avaliacao(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid da avaliação a fazer get")]
):
    """
    Requisita uma avaliação de produto específica com base no UUID.

    Args:
        uuid (str): O UUID da avaliação.

    Returns:
        AvaliacaoDeProduto: A avaliação de produto correspondente ao UUID.
    """
    repository = Repository(AvaliacaoDeProduto, connection=connection)
    result = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_avaliacoes(
    connection: connection_dependency,
    avaliacao: AvaliacaoDeProduto
):
    """
    Cadastra uma nova avaliação de produto.

    Args:
        avaliacao (AvaliacaoDeProduto): Os dados da avaliação a ser cadastrada.

    Returns:
        dict: Um dicionário contendo o UUID da avaliação cadastrada.
    """
    repository = Repository(AvaliacaoDeProduto, connection=connection)
    try:
        uuid = await repository.save(avaliacao)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_avaliacao_put(
    connection: connection_dependency,
    avaliacaoData: AvaliacaoDeProduto,
    uuid: Annotated[str, Path(title="O uuid da avaliação a fazer put")],
):
    """
    Atualiza uma avaliação de produto utilizando o método PUT.

    Args:
        avaliacaoData (AvaliacaoDeProduto): Os dados atualizados da avaliação.
        uuid (str): O UUID da avaliação a ser atualizada.

    Returns:
        dict: Um dicionário contendo o número de linhas afetadas pela atualização.
    """
    repository = Repository(AvaliacaoDeProduto, connection=connection)
    avaliacao = await repository.find_one(uuid=uuid)
    if avaliacao is None:
        raise NotFoundException
    
    num_rows_affected = await repository.update(
        avaliacao, avaliacaoData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_avaliacao_patch(
    avaliacaoData: AvaliacaoDeProduto,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do avaliação a fazer patch")]
):
    repository = Repository(AvaliacaoDeProduto, connection=connection)
    avaliacao = await repository.find_one(uuid=uuid)
    if avaliacao is None:
        raise NotFoundException
    
    num_rows_affected = await repository.update(
        avaliacao,
        avaliacaoData.model_dump()  # type: ignore
    )

    return {'num_rows_affected': num_rows_affected}


@router.delete("/{uuid}")
async def remover_avaliacao(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid da avaliação a fazer delete")]
):
    """
    Remove uma avaliação de produto com base no UUID.

    Args:
        uuid (str): O UUID da avaliação a ser removida.

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    repository = Repository(AvaliacaoDeProduto, connection=connection)
    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
