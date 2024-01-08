from typing import Annotated, Dict, Optional, Any
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Response
)
from src.models import (
    PedidoGET,
    PedidoPOST,
    AlterarStatusPedidoPATCH,
)
from src.dependencies import (
    pedido_service_dependency,
    current_company
)


router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.get("/")
async def requisitar_pedidos(
    service: pedido_service_dependency,
    loja_uuid: Optional[str] = Query(None),
    usuario_uuid: Optional[str] = Query(None)
):
    """
    Obtém uma lista de todos os pedidos cadastrados.

    Args:
        loja_uuid (str, opcional): UUID da loja para filtrar os pedidos.

    Returns:
        list: Uma lista contendo os pedidos encontrados.
    """
    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid
    if usuario_uuid is not None:
        kwargs["usuario_uuid"] = usuario_uuid

    pedidos_itens = await service.get_all_pedidos(**kwargs)
    return pedidos_itens


@router.get("/{uuid}")
async def requisitar_pedido(
    service: pedido_service_dependency,
    uuid: Annotated[str, Path(title="O uuid do pedido a fazer get")]
) -> PedidoGET:
    """
    Obtém detalhes de um pedido pelo seu UUID.

    Args:
        uuid (str): UUID do pedido.

    Returns:
        Pedido: Os detalhes do pedido.
    """

    pedido = await service.get_pedido(uuid)
    if pedido is None or pedido.uuid is None:
        raise NotFoundException("Pedido não encontrado")

    return pedido


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_pedidos(
    pedido_data: PedidoPOST,
    service: pedido_service_dependency,
) -> Dict[str, Any]:
    """
    Cadastra um novo pedido.

    Args:
        pedido (Pedido): Dados do pedido a ser cadastrado.

    Returns:
        dict: Um dicionário contendo o UUID do pedido cadastrado.
    """
    try:
        response = await service.save_pedido(pedido_data=pedido_data)
        return response
    except Exception as error:

        import traceback
        traceback.print_exc()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Erro no cadastro do pedido! detail: {error}'
        )


@router.patch("/alterar_status_de_pedido/{uuid}")
async def alterar_status_de_pedido(
    current_company: current_company,
    service: pedido_service_dependency,
    data: AlterarStatusPedidoPATCH,
    uuid: Annotated[str, Path(title="O uuid do pedido a fazer patch")],
):
    try:
        await service.alterar_status_de_pedido(
            pedido_uuid=uuid,
            status_uuid=data.status_uuid
        )
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Erro no cadastro do pedido! detail: {error}'
        )


@router.patch("/concluir_pedido/{uuid}")
async def concluir_pedido(
    current_company: current_company,
    response: Response,
    service: pedido_service_dependency,
    uuid: Annotated[str, Path(title="O uuid do pedido a fazer patch")],
):

    try:
        await service.concluir_pedido(pedido_uuid=uuid)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Erro no cadastro do pedido! detail: {error}'
        )


@router.delete("/{uuid}")
async def remover_pedido(
    current_company: current_company,
    service: pedido_service_dependency,
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

    try:
        response = await service.remover_pedido(uuid=uuid)
        return response
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
