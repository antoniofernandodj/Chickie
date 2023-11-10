from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path
)
from src.schemas import Endereco
from src.infra.database_postgres.repository import Repository
from src.dependencies import (
    connection_dependency
)

router = APIRouter(prefix="/enderecos", tags=["Endereços"])

NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Endereço não encontrado"
)

@router.get("/")
async def requisitar_enderecos(connection: connection_dependency):
    """
    Requisita todos os endereços cadastrados.

    Returns:
        List[Endereco]: Uma lista contendo todos os endereços cadastrados.
    """
    repository = Repository(Endereco, connection=connection)
    results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_endereco(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do endereço a fazer get")]
):
    """
    Requisita um endereço específico com base no UUID.

    Args:
        uuid (str): O UUID do endereço.

    Returns:
        Endereco: O endereço correspondente ao UUID.
    """
    repository = Repository(Endereco, connection=connection)
    result = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_enderecos(
    connection: connection_dependency,
    endereco: Endereco
):
    """
    Cadastra um novo endereço.

    Args:
        endereco (Endereco): Os dados do endereço a ser cadastrado.

    Returns:
        dict: Um dicionário contendo o UUID do endereço cadastrado.
    """
    repository = Repository(Endereco, connection=connection)
    try:
        uuid = await repository.save(endereco)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.patch("/{uuid}")
async def atualizar_endereco_patch(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do endereço a fazer patch")]
):
    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_endereco_put(
    itemData: Endereco,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do endereco a fazer put")],
):
    """
    Atualiza um endereço utilizando o método PUT.

    Args:
        itemData (Endereco): Os dados atualizados do endereço.
        uuid (str): O UUID do endereço a ser atualizado.

    Returns:
        dict: Um dicionário contendo o número de linhas afetadas pela atualização.
    """
    repository = Repository(Endereco, connection=connection)
    endereco = await repository.find_one(uuid=uuid)
    if endereco is None:
        raise NotFoundException
    
    num_rows_affected = await repository.update(
        endereco, itemData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_endereco(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do endereço a fazer delete")]
):
    """
    Remove um endereço com base no UUID.

    Args:
        uuid (str): O UUID do endereço a ser removido.

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    repository = Repository(Endereco, connection=connection)
    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
