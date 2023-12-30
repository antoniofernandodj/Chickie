from typing import Annotated
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path
)
from src.schemas import Feedback
from src.infra.database_postgres.repository import Repository
from src.dependencies import (
    connection_dependency
)


router = APIRouter(prefix="/feedbacks", tags=["Feedbacks"])


@router.get("/")
async def requisitar_feedbacks(connection: connection_dependency):
    """
    Requisita todos os feedbacks cadastrados.

    Returns:
        List[Feedback]: Uma lista contendo todos os feedbacks cadastrados.
    """
    repository = Repository(Feedback, connection=connection)
    results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_feedback(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do feedback a fazer get")]
):
    """
    Requisita um feedback específico com base no UUID.

    Args:
        uuid (str): O UUID do feedback.

    Returns:
        Feedback: O feedback correspondente ao UUID.
    """
    repository = Repository(Feedback, connection=connection)
    result = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Feedback não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_feedbacks(
    connection: connection_dependency,
    feedback: Feedback,
):
    """
    Cadastra um novo feedback.

    Args:
        feedback (Feedback): Os dados do feedback a ser cadastrado.

    Returns:
        dict: Um dicionário contendo o UUID do feedback cadastrado.
    """
    repository = Repository(Feedback, connection=connection)
    try:
        uuid = await repository.save(feedback)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_feedback_put(
    feedbackData: Feedback,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do feedback a fazer put")],
):
    """
    Atualiza um feedback utilizando o método PUT.

    Args:
        feedbackData (Feedback): Os dados atualizados do feedback.
        uuid (str): O UUID do feedback a ser atualizado.

    Returns:
        dict: Um dicionário contendo o número de linhas
        afetadas pela atualização.
    """
    repository = Repository(Feedback, connection=connection)
    feedback = await repository.find_one(uuid=uuid)
    if feedback is None:
        raise NotFoundException("Feedback não encontrado")

    num_rows_affected = await repository.update(
        feedback, feedbackData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_feedback_patch(
    feedbackData: Feedback,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do feedback a fazer patch")],
):
    repository = Repository(Feedback, connection=connection)
    feedback = await repository.find_one(uuid=uuid)
    if feedback is None:
        raise NotFoundException("Feedback não encontrado")

    num_rows_affected = await repository.update(
        feedback, feedbackData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_feedback(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do feedback a fazer delete")]
):
    """
    Remove um feedback com base no UUID.

    Args:
        uuid (str): O UUID do feedback a ser removido.

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    repository = Repository(Feedback, connection=connection)
    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
