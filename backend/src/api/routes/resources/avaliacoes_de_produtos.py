#
from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Depends,
    Query,
)
from src.api import security
from src.schemas import Loja, AvaliacaoDeProduto
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


current_user = Annotated[Loja, Depends(security.current_user)]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Avaliação não encontrada"
)

router = APIRouter(
    prefix="/avaliacoes-de-produtos",
    tags=["Avaliações de produtos"]
)


@router.get("/")
async def requisitar_avaliacoes():
    """
    Requisita todas as avaliações de produtos.

    Returns:
        List[AvaliacaoDeProduto]: Uma lista contendo todas as avaliações de produtos.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(AvaliacaoDeProduto, connection=connection)
        results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_avaliacao(
    uuid: Annotated[str, Path(title="O uuid da avaliação a fazer get")]
):
    """
    Requisita uma avaliação de produto específica com base no UUID.

    Args:
        uuid (str): O UUID da avaliação.

    Returns:
        AvaliacaoDeProduto: A avaliação de produto correspondente ao UUID.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(AvaliacaoDeProduto, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_avaliacoes(avaliacao: AvaliacaoDeProduto):
    """
    Cadastra uma nova avaliação de produto.

    Args:
        avaliacao (AvaliacaoDeProduto): Os dados da avaliação a ser cadastrada.

    Returns:
        dict: Um dicionário contendo o UUID da avaliação cadastrada.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(AvaliacaoDeProduto, connection=connection)
        try:
            uuid = await repository.save(avaliacao)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_avaliacao_put(
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
    async with DatabaseConnectionManager() as connection:
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
    uuid: Annotated[str, Path(title="O uuid do avaliação a fazer patch")]
):
    async with DatabaseConnectionManager() as connection:
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
    uuid: Annotated[str, Path(title="O uuid da avaliação a fazer delete")]
):
    """
    Remove uma avaliação de produto com base no UUID.

    Args:
        uuid (str): O UUID da avaliação a ser removida.

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(AvaliacaoDeProduto, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
