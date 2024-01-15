from typing import Annotated, Optional, Dict, List
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query
)
from src.domain.models import Status
from src.dependencies import (
    status_repository_dependency,
    current_company
)


router = APIRouter(prefix="/status", tags=["Status"])


@router.get("/")
async def requisitar_varios_status(
    repository: status_repository_dependency,
    loja_uuid: Optional[str] = Query(None)
) -> List[Status]:

    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results: List[Status] = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_status(
    repository: status_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do status a fazer get")]
) -> Status:

    result: Optional[Status] = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Status não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_status(
    status: Status,
    current_company: current_company,
    repository: status_repository_dependency
) -> Dict[str, str]:

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
) -> Dict[str, int]:

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
) -> Dict:
    return {}


@router.delete("/{uuid}")
async def remover_status(
    current_company: current_company,
    repository: status_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do status a fazer delete")]
) -> Dict[str, int]:

    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
