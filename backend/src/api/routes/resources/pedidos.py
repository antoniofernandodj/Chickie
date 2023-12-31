from typing import Annotated, List, Dict, Optional, Any
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query
)
from src.schemas import Pedido, PedidoItens, ItemPedido, Endereco, Status
from src.dependencies import (
    pedido_repository_dependency,
    endereco_repository_dependency,
    status_repository_dependency,
    item_pedido_repository_dependency,
    connection_dependency,
    current_company
)


router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.get("/")
async def requisitar_pedidos(
    pedido_repository: pedido_repository_dependency,
    itens_repository: item_pedido_repository_dependency,
    endereco_repository: endereco_repository_dependency,
    status_repository: status_repository_dependency,
    current_company: current_company,
    loja_uuid: Optional[str] = Query(None)
) -> List[PedidoItens]:
    """
    Obtém uma lista de todos os pedidos cadastrados.

    Args:
        loja_uuid (str, opcional): UUID da loja para filtrar os pedidos.

    Returns:
        list: Uma lista contendo os pedidos encontrados.
    """
    pedidos_itens: List[PedidoItens] = []
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid

    pedidos: List[PedidoItens] = await pedido_repository.find_all(**kwargs)

    for pedido in pedidos:
        items: List[ItemPedido] = await itens_repository.find_all(
            pedido_uuid=pedido.uuid
        )

        status: Optional[Status] = await status_repository.find_one(
            uuid=pedido.status_uuid
        )

        endereco: Optional[Endereco] = await endereco_repository.find_one(
            uuid=pedido.endereco_uuid
        )

        if endereco is None:
            continue

        pedido_itens = PedidoItens(
            status_uuid=pedido.status_uuid,
            status=status,
            celular=pedido.celular,
            frete=pedido.frete,
            loja_uuid=pedido.loja_uuid,
            endereco=endereco,
            uuid=pedido.uuid,
            itens_pedido=items,
            data_hora=pedido.data_hora
        )
        pedidos_itens.append(pedido_itens)

    return pedidos_itens


@router.get("/{uuid}")
async def requisitar_pedido(
    pedido_repository: pedido_repository_dependency,
    endereco_repository: endereco_repository_dependency,
    itens_repository: item_pedido_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do pedido a fazer get")]
) -> PedidoItens:
    """
    Obtém detalhes de um pedido pelo seu UUID.

    Args:
        uuid (str): UUID do pedido.

    Returns:
        Pedido: Os detalhes do pedido.
    """
    pedido: Optional[Any] = await pedido_repository.find_one(uuid=uuid)
    if pedido is None:
        raise NotFoundException("Pedido não encontrado")

    items: List[ItemPedido] = await itens_repository.find_all(pedido_uuid=uuid)

    print({'items': await itens_repository.find_all()})
    print({'items': items})

    endereco: Optional[Endereco] = await endereco_repository.find_one(
        uuid=pedido.endereco_uuid
    )

    print({'endereco': endereco})

    if endereco is None:
        raise NotFoundException('Endereco de pedido não encontrado')

    response = PedidoItens(
        status_uuid=pedido.status_uuid,
        frete=pedido.frete,
        celular=pedido.celular,
        loja_uuid=pedido.loja_uuid,
        uuid=pedido.uuid,
        itens_pedido=items,
        data_hora=pedido.data_hora,
        endereco=endereco
    )

    print({'response': response})

    return response


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_pedidos(
    pedido: PedidoItens,
    pedido_repository: pedido_repository_dependency,
    itens_repository: item_pedido_repository_dependency,
    endereco_repository: endereco_repository_dependency
) -> Dict[str, Any]:
    """
    Cadastra um novo pedido.

    Args:
        pedido (Pedido): Dados do pedido a ser cadastrado.

    Returns:
        dict: Um dicionário contendo o UUID do pedido cadastrado.
    """
    itens = pedido.itens_pedido
    if pedido.endereco_uuid is None:
        pedido.endereco_uuid = await endereco_repository.save(
            model=pedido.endereco
        )

    del pedido.itens_pedido
    del pedido.endereco

    itens_uuid = []
    try:
        pedido_uuid = await pedido_repository.save(pedido)
        print({'pedido_uuid': pedido_uuid})
        for item in itens:
            item.pedido_uuid = pedido_uuid
            item.loja_uuid = pedido.loja_uuid
            item_uuid = await itens_repository.save(item)
            print({'item_uuid': item_uuid})
            itens_uuid.append(item_uuid)

    except Exception as error:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(error))

    response = {"pedido_uuid": pedido_uuid, 'itens_uuid': itens_uuid}
    print({'response': response})
    return response


@router.patch("/{uuid}")
async def atualizar_pedido_patch(
    current_company: current_company,
    pedido_repository: pedido_repository_dependency,
    itens_repository: item_pedido_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do pedido a fazer patch")],
) -> Dict[str, str]:
    return {"uuid": uuid}


@router.put("/{uuid}")
async def atualizar_pedido_put(
    itemData: Pedido,
    pedido_repository: pedido_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid do pedido a fazer put")],
    current_company: current_company,
) -> Dict[str, int]:
    """
    Atualiza um pedido completamente usando PUT.

    Args:
        itemData (Pedido): Dados do pedido para atualização.
        uuid (str): UUID do pedido a ser atualizado.
        current_company (Loja): Dados da loja autenticada (dependência).

    Returns:
        dict: Um dicionário contendo o número de linhas
        afetadas na atualização.
    """
    pedido = await pedido_repository.find_one(uuid=uuid)
    if pedido is None:
        raise NotFoundException("Pedido não encontrado")

    num_rows_affected = await pedido_repository.update(
        pedido, itemData.model_dump()  # type: ignore
    )

    return {"num_rows_affected": num_rows_affected}


@router.delete("/{uuid}")
async def remover_pedido(
    current_company: current_company,
    pedido_repository: pedido_repository_dependency,
    itens_repository: item_pedido_repository_dependency,
    connection: connection_dependency,
    uuid: Annotated[str, Path(title="O uuid do pedido a fazer delete")]
) -> Dict[str, int]:
    """
    Remove um pedido.

    Args:
        uuid (str): UUID do pedido a ser removido.
        current_company (Loja): Dados da loja autenticada (dependência).

    Returns:
        dict: Um dicionário contendo o número de itens removidos.
    """
    itens_removed = 0
    pedidos_removed = 0

    try:
        itens_pedido: List[ItemPedido] = await itens_repository.find_all(
            pedido_uuid=uuid
        )
        for item in itens_pedido:
            if item.uuid is None:
                continue
            i = await itens_repository.delete_from_uuid(
                uuid=item.uuid
            )
            itens_removed += i
        pedidos_removed = await pedido_repository.delete_from_uuid(
            uuid=uuid
        )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

    return {
        "pedidos_removed": pedidos_removed,
        'itens_removed': itens_removed
    }
