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
from src.schemas import Loja, MetodoDePagamento
from src.infra.database.repository import Repository
from src.infra.database.manager import DatabaseConnectionManager


current_company = Annotated[Loja, Depends(security.current_company)]
NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Metodo de pagamento não encontrado",
)

router = APIRouter(
    prefix="/metodos_de_pagamento", tags=["Métodos de pagamentos"]
)


@router.get("/")
async def requisitar_metodos_de_pagamento(
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
    async with DatabaseConnectionManager() as connection:
        repository = Repository(MetodoDePagamento, connection=connection)
        results = await repository.find_all()

    return results


@router.get("/{uuid}")
async def requisitar_metodo_de_pagamento(
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
    async with DatabaseConnectionManager() as connection:
        repository = Repository(MetodoDePagamento, connection=connection)
        result = await repository.find_one(uuid=uuid)

        if result is None:
            raise NotFoundException

    return result


@router.post("/", status_code=201)
async def cadastrar_metodos_de_pagamento(
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
    async with DatabaseConnectionManager() as connection:
        repository = Repository(MetodoDePagamento, connection=connection)
        try:
            uuid = await repository.save(metodo_de_pagamento)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_metodo_de_pagamento_put(
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
    async with DatabaseConnectionManager() as connection:
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
    metodo_de_pagamentoData: MetodoDePagamento,
    current_company: current_company,
    uuid: Annotated[
        str, Path(title="O uuid do método de pagemento a fazer patch")
    ],
):
    async with DatabaseConnectionManager() as connection:
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
    async with DatabaseConnectionManager() as connection:
        repository = Repository(MetodoDePagamento, connection=connection)
        try:
            itens_removed = await repository.delete_from_uuid(uuid=uuid)
        except Exception as error:
            raise HTTPException(status_code=500, detail=str(error))

    return {"itens_removed": itens_removed}
