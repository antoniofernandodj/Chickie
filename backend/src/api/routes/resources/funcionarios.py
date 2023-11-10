from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query
)
from typing import Optional
from src.schemas import Funcionario
from src.infra.database_postgres.repository import Repository
from src.dependencies import (
    connection_dependency,
    current_company
)


router = APIRouter(prefix="/funcionarios", tags=["Funcionários"])

NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Funcionario não encontrado"
)

@router.get("/")
async def requisitar_funcionarios(
    connection: connection_dependency,
    loja_uuid: Optional[str] = Query(None)
):
    """
    Requisita todos os funcionários cadastrados, com opção de filtro por UUID da loja.

    Args:
        loja_uuid (str, optional): O UUID da loja para filtrar os funcionários.

    Returns:
        List[Funcionario]: Uma lista contendo todos os funcionários cadastrados.
    """
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    repository = Repository(Funcionario, connection=connection)
    results = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_funcionario(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do funcionário a fazer get")]
):
    """
    Requisita um funcionário específico com base no UUID.

    Args:
        uuid (str): O UUID do funcionário.

    Returns:
        Funcionario: O funcionário correspondente ao UUID.
    """

    repository = Repository(Funcionario, connection=connection)
    result = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException
    
    return result


@router.post("/", status_code=201)
async def cadastrar_funcionarios(
    funcionario: Funcionario,
    current_company: current_company,
    connection: connection_dependency
):
    """
    Cadastra um novo funcionário.

    Args:
        funcionario (Funcionario): Os dados do funcionário a ser cadastrado.
        current_company (Loja): Dados da loja autenticada (dependência).

    Returns:
        dict: Um dicionário contendo o UUID do funcionário cadastrado.
    """
    repository = Repository(Funcionario, connection=connection)
    try:
        uuid = await repository.save(funcionario)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_funcionario_put(
    funcionarioData: Funcionario,
    current_company: current_company,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do funcionario a fazer put")]
):
    """
    Atualiza os dados de um funcionário utilizando o método HTTP PUT.

    Args:
        current_company (Loja): Dados da loja autenticada (dependência).
        funcionarioData (Funcionario): Os novos dados do funcionário.
        uuid (str): O UUID do funcionário a ser atualizado.

    Returns:
        dict: Um dicionário contendo o número de linhas afetadas na atualização.
    """
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
    current_company: current_company,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do funcionario a fazer patch")],
):
    repository = Repository(Funcionario, connection=connection)
    funcionario = await repository.find_one(uuid=uuid)
    if funcionario is None:
        raise NotFoundException
    
    num_rows_affected = await repository.update(
        funcionario, funcionarioData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_funcionario(
    current_company: current_company,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do funcionario a fazer delete")],
):
    """
    Remove um funcionário cadastrado.

    Args:
        current_company (Loja): Dados da loja autenticada (dependência).
        uuid (str): O UUID do funcionário a ser removido.

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    repository = Repository(Funcionario, connection=connection)
    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
