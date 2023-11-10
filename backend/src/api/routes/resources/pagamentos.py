from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query
)
from typing import Optional
from src.schemas import Pagamento
from src.infra.database_postgres.repository import Repository
from src.dependencies import (
    connection_dependency
)

router = APIRouter(prefix="/pagamentos", tags=["Pagamentos"])

NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Pagamento não encontrado"
)

@router.get("/")
async def requisitar_pagamentos(
    connection: connection_dependency,
    loja_uuid: Optional[str] = Query(None)
):
    """
    Requisita pagamentos cadastrados na plataforma.
    
    Args:
        loja_uuid (Optional[str]): O uuid da loja, caso necessário.
    
    Returns:
        list[Pagamento]: Lista de pagamentos encontrados.
    """
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    repository = Repository(Pagamento, connection=connection)
    results = await repository.find_all(**kwargs)

    return results


@router.get("/{uuid}")
async def requisitar_pagamento(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do pagamento a fazer get")]
):
    """
    Busca um pagamento pelo seu uuid.
    
    Args:
        uuid (str): O uuid do pagamento a ser buscado.
    
    Returns:
        Pagamento: O pagamento encontrado.
    
    Raises:
        HTTPException: Se o pagamento não for encontrado.
    """
    repository = Repository(Pagamento, connection=connection)
    result = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_pagamentos(
    connection: connection_dependency,
    pagamento: Pagamento
):
    """
    Cadastra um novo pagamento na plataforma.
    
    Args:
        pagamento (Pagamento): Os detalhes do pagamento a ser cadastrado.
    
    Returns:
        dict: Um dicionário contendo o uuid do pagamento cadastrado.
    
    Raises:
        HTTPException: Se ocorrer um erro durante o cadastro.
    """
    repository = Repository(Pagamento, connection=connection)
    try:
        uuid = await repository.save(pagamento)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_pagamento_put(
    pagamento_Data: Pagamento,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do pagemento a fazer put")],
):
    """
    Atualiza um pagamento utilizando o método HTTP PUT.
    
    Args:
        pagamento_Data (Pagamento): Os novos dados do pagamento.
        uuid (str): O uuid do pagamento a ser atualizado.
    
    Returns:
        dict: Um dicionário contendo o número de linhas afetadas na atualização.
    
    Raises:
        HTTPException: Se o pagamento não for encontrado.
    """
    repository = Repository(Pagamento, connection=connection)
    pagamento = await repository.find_one(uuid=uuid)
    if pagamento is None:
        raise NotFoundException
    
    num_rows_affected = await repository.update(
        pagamento, pagamento_Data.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_pagamento_patch(
    pagamentoData: Pagamento,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do pagamento a fazer patch")],
):
    repository = Repository(Pagamento, connection=connection)
    pagamento = await repository.find_one(uuid=uuid)
    if pagamento is None:
        raise NotFoundException
    
    num_rows_affected = await repository.update(
        pagamento, pagamentoData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_pagamento(
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do pagemento a fazer delete")]
):
    """
    Remove um pagamento pelo seu uuid.
    
    Args:
        uuid (str): O uuid do pagamento a ser removido.
    
    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    
    Raises:
        HTTPException: Se ocorrer um erro durante a remoção.
    """
    repository = Repository(Pagamento, connection=connection)
    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
