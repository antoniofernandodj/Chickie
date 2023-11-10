from typing import Annotated
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query
)
from typing import Optional
from src.schemas import MetodoDePagamento
from src.infra.database_postgres.repository import Repository
from src.dependencies import (
    connection_dependency,
    current_company
)


router = APIRouter(
    prefix="/metodos_de_pagamento", tags=["Métodos de pagamentos"]
)

NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Metodo de pagamento não encontrado",
)

@router.get("/")
async def requisitar_metodos_de_pagamento(
    connection: connection_dependency,
    loja_uuid: Optional[str] = Query(None),
):
    """
    Obtém uma lista de todos os métodos de pagamento cadastrados.

    Args:
        loja_uuid (str, opcional): UUID da loja para filtrar os métodos de pagamento.

    Returns:
        list: Uma lista contendo os métodos de pagamento encontrados.
    """
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    repository = Repository(MetodoDePagamento, connection=connection)
    results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_metodo_de_pagamento(
    connection: connection_dependency,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagamento a fazer get")
    ]
):
    """
    Obtém detalhes de um método de pagamento pelo seu UUID.

    Args:
        uuid (str): UUID do método de pagamento.

    Returns:
        MetodoDePagamento: Os detalhes do método de pagamento.
    """
    repository = Repository(MetodoDePagamento, connection=connection)
    result = await repository.find_one(uuid=uuid)
    if result is None:
        raise NotFoundException
    
    return result


@router.post("/", status_code=201)
async def cadastrar_metodos_de_pagamento(
    connection: connection_dependency,
    metodo_de_pagamento: MetodoDePagamento,
    current_company: current_company,
):
    """
    Cadastra um novo método de pagamento.

    Args:
        metodo_de_pagamento (MetodoDePagamento): Dados do método de pagamento a ser cadastrado.
        current_company (Loja): Dados da loja autenticada (dependência).

    Returns:
        dict: Um dicionário contendo o UUID do método de pagamento cadastrado.
    """
    repository = Repository(MetodoDePagamento, connection=connection)
    try:
        uuid = await repository.save(metodo_de_pagamento)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_metodo_de_pagamento_put(
    connection: connection_dependency,
    metodo_de_pagamento_Data: MetodoDePagamento,
    current_company: current_company,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer put")
    ],
):
    """
    Atualiza os dados de um método de pagamento utilizando o método HTTP PUT.

    Args:
        metodo_de_pagamento_Data (MetodoDePagamento): Os novos dados do método de pagamento.
        current_company (Loja): Dados da loja autenticada (dependência).
        uuid (str): O UUID do método de pagamento a ser atualizado.

    Returns:
        dict: Um dicionário contendo o número de linhas afetadas na atualização.
    """
    repository = Repository(MetodoDePagamento, connection=connection)
    metodo_de_pagamento = await repository.find_one(uuid=uuid)
    if metodo_de_pagamento is None:
        raise NotFoundException
    
    num_rows_affected = await repository.update(
        metodo_de_pagamento,
        metodo_de_pagamento_Data.model_dump(),  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.patch("/{uuid}")
async def atualizar_metodo_de_pagamento_patch(
    connection: connection_dependency,
    metodo_de_pagamentoData: MetodoDePagamento,
    current_company: current_company,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer patch")
    ],
):
    repository = Repository(MetodoDePagamento, connection=connection)
    metodo_de_pagamento = await repository.find_one(uuid=uuid)
    if metodo_de_pagamento is None:
        raise NotFoundException
    num_rows_affected = await repository.update(
        metodo_de_pagamento,
        metodo_de_pagamentoData.model_dump(),  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_metodo_de_pagamento(
    connection: connection_dependency,
    current_company: current_company,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer delete")
    ],
):
    """
    Remove um método de pagamento cadastrado.

    Args:
        current_company (Loja): Dados da loja autenticada (dependência).
        uuid (str): O UUID do método de pagamento a ser removido.

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    repository = Repository(MetodoDePagamento, connection=connection)
    try:
        itens_removed = await repository.delete_from_uuid(uuid=uuid)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
