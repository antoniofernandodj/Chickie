from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Depends,
    Query,
)
from src.main import security
from src.schemas import Loja, Funcionario
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


current_user = Annotated[Loja, Depends(security.current_user)]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Funcionario não encontrado"
)

router = APIRouter(
    prefix="/funcionarios",
    tags=["Funcionários"]
)


@router.get("/")
async def requisitar_funcionarios():
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Funcionario, connection=connection)
        results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_funcionario(
    uuid: Annotated[str, Path(title="O uuid do funcionário a fazer get")]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Funcionario, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_funcionarios(funcionario: Funcionario):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Funcionario, connection=connection)
        try:
            uuid = await repository.save(funcionario)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_funcionario_put(
    funcionarioData: Funcionario,
    uuid: Annotated[str, Path(title="O uuid do funcionario a fazer put")],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Funcionario, connection=connection)
        funcionario = await repository.find_one(uuid=uuid)
        if funcionario is None:
            raise NotFoundException

    num_rows_affected = await repository.update(
        funcionario, funcionarioData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_funcionario_patch(
    funcionarioData: Funcionario,
    uuid: Annotated[str, Path(title="O uuid do funcionario a fazer patch")]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Funcionario, connection=connection)
        funcionario = await repository.find_one(uuid=uuid)
        if funcionario is None:
            raise NotFoundException

    num_rows_affected = await repository.update(
        funcionario,
        funcionarioData.model_dump()  # type: ignore
    )

    return {'num_rows_affected': num_rows_affected}


@router.delete("/{uuid}")
async def remover_funcionario(
    uuid: Annotated[str, Path(title="O uuid do funcionario a fazer delete")]
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Funcionario, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
