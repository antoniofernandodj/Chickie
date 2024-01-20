from typing import Annotated
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Request
)
from typing import Optional
from src.domain.models import Funcionario
from src.infra.database_postgres.repository import Repository
from src.dependencies import (
    current_company
)
from src.dependencies.connection_dependency import connection_dependency


router = APIRouter(prefix="/funcionarios", tags=["Funcionários"])


@router.get("/")
async def requisitar_funcionarios(
    request: Request,
    connection: connection_dependency,
    loja_uuid: Optional[str] = Query(None)
):

    repository = Repository(Funcionario, connection=connection)

    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    results = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_funcionario(
    request: Request,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do funcionário a fazer get")]
):

    repository = Repository(Funcionario, connection=connection)

    result = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException("Funcionario não encontrado")

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_funcionarios(
    request: Request,
    funcionario: Funcionario,
    current_company: current_company,
    connection: connection_dependency
):

    repository = Repository(Funcionario, connection=connection)

    try:
        uuid = await repository.save(funcionario)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_funcionario_put(
    request: Request,
    funcionarioData: Funcionario,
    current_company: current_company,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do funcionario a fazer put")]
):

    repository = Repository(Funcionario, connection=connection)

    funcionario = await repository.find_one(uuid=uuid)
    if funcionario is None:
        raise NotFoundException("Funcionario não encontrado")

    num_rows_affected = await repository.update(
        funcionario, funcionarioData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_funcionario_patch(
    request: Request,
    funcionarioData: Funcionario,
    current_company: current_company,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do funcionario a fazer patch")],
):
    repository = Repository(Funcionario, connection=connection)

    funcionario = await repository.find_one(uuid=uuid)
    if funcionario is None:
        raise NotFoundException("Funcionario não encontrado")

    num_rows_affected = await repository.update(
        funcionario, funcionarioData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_funcionario(
    request: Request,
    current_company: current_company,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do funcionario a fazer delete")],
):

    repository = Repository(Funcionario, connection=connection)

    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
