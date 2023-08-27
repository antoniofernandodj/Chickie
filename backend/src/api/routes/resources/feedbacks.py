from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Depends,
    Query,
)
from src.schemas import Feedback
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Feedback não encontrado"
)

router = APIRouter(prefix="/feedbacks", tags=["Feedbacks"])


@router.get("/")
async def requisitar_feedbacks():
    """
    Requisita todos os feedbacks cadastrados.

    Returns:
        List[Feedback]: Uma lista contendo todos os feedbacks cadastrados.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Feedback, connection=connection)
        results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_feedback(
    uuid: Annotated[str, Path(title="O uuid do feedback a fazer get")]
):
    """
    Requisita um feedback específico com base no UUID.

    Args:
        uuid (str): O UUID do feedback.

    Returns:
        Feedback: O feedback correspondente ao UUID.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Feedback, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_feedbacks(feedback: Feedback):
    """
    Cadastra um novo feedback.

    Args:
        feedback (Feedback): Os dados do feedback a ser cadastrado.

    Returns:
        dict: Um dicionário contendo o UUID do feedback cadastrado.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Feedback, connection=connection)
        try:
            uuid = await repository.save(feedback)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_feedback_put(
    feedbackData: Feedback,
    uuid: Annotated[str, Path(title="O uuid do feedback a fazer put")],
):
    """
    Atualiza um feedback utilizando o método PUT.

    Args:
        feedbackData (Feedback): Os dados atualizados do feedback.
        uuid (str): O UUID do feedback a ser atualizado.

    Returns:
        dict: Um dicionário contendo o número de linhas afetadas pela atualização.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Feedback, connection=connection)
        feedback = await repository.find_one(uuid=uuid)
        if feedback is None:
            raise NotFoundException

        num_rows_affected = await repository.update(
            feedback, feedbackData.model_dump()  # type: ignore
        )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_feedback_patch(
    feedbackData: Feedback,
    uuid: Annotated[str, Path(title="O uuid do feedback a fazer patch")],
):

    async with DatabaseConnectionManager() as connection:
        repository = Repository(Feedback, connection=connection)
        feedback = await repository.find_one(uuid=uuid)
        if feedback is None:
            raise NotFoundException

    num_rows_affected = await repository.update(
        feedback, feedbackData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_feedback(
    uuid: Annotated[str, Path(title="O uuid do feedback a fazer delete")]
):
    """
    Remove um feedback com base no UUID.

    Args:
        uuid (str): O UUID do feedback a ser removido.

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Feedback, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
