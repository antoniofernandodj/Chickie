#
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
from typing import Optional
from src.api import security
from src.schemas import Loja, Entregador
from src.infra.database_postgres.repository import Repository
from src.infra.database_postgres.manager import DatabaseConnectionManager


current_company = Annotated[Loja, Depends(security.current_company)]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Entregador não encontrado"
)

router = APIRouter(prefix="/entregadores", tags=["Entregadores"])


@router.get("/")
async def requisitar_entregadores(loja_uuid: Optional[str] = Query(None)):
    """
    Requisita todos os entregadores cadastrados.

    Args:
        loja_uuid (str, optional): O UUID da loja para filtrar os entregadores. Default é None.

    Returns:
        List[Entregador]: Uma lista contendo todos os entregadores cadastrados.
    """
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Entregador, connection=connection)
        results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_entregador(
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer get")]
):
    """
    Requisita um entregador específico com base no UUID.

    Args:
        uuid (str): O UUID do entregador.

    Returns:
        Entregador: O entregador correspondente ao UUID.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Entregador, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_entregadores(
    entregador: Entregador,
    current_company: current_company,
):
    """
    Cadastra um novo entregador.

    Args:
        entregador (Entregador): Os dados do entregador a ser cadastrado.
        current_company (Loja): A loja atual, obtida através do token de autenticação.

    Returns:
        dict: Um dicionário contendo o UUID do entregador cadastrado.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Entregador, connection=connection)
        try:
            uuid = await repository.save(entregador)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_entregador_put(
    current_company: current_company,
    entregadorData: Entregador,
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer put")],
):
    """
    Atualiza um entregador utilizando o método PUT.

    Args:
        current_company (Loja): A loja atual, obtida através do token de autenticação.
        entregadorData (Entregador): Os dados atualizados do entregador.
        uuid (str): O UUID do entregador a ser atualizado.

    Returns:
        dict: Um dicionário contendo o número de linhas afetadas pela atualização.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Entregador, connection=connection)
        entregador = await repository.find_one(uuid=uuid)
        if entregador is None:
            raise NotFoundException

        num_rows_affected = await repository.update(
            entregador, entregadorData.model_dump()  # type: ignore
        )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_entregador_patch(
    current_company: current_company,
    entregadorData: Entregador,
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer patch")],
):
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Entregador, connection=connection)
        entregador = await repository.find_one(uuid=uuid)
        if entregador is None:
            raise NotFoundException

    num_rows_affected = await repository.update(
        entregador, entregadorData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_entregador(
    current_company: current_company,
    uuid: Annotated[str, Path(title="O uuid do entregador a fazer delete")],
):
    """
    Remove um entregador com base no UUID.

    Args:
        current_company (Loja): A loja atual, obtida através do token de autenticação.
        uuid (str): O UUID do entregador a ser removido.

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    async with DatabaseConnectionManager() as connection:
        repository = Repository(Entregador, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
