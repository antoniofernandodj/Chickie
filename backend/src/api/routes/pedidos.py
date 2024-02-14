from typing import Annotated, Optional
from src.exceptions import (
    NotFoundException
)
from fastapi import (  # type: ignore  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Response
)
from src.domain.models import (
    PedidoGET,
    PedidoPOST,
    Pedidos,
    AlterarStatusPedidoPATCH,
)
from src.misc import Paginador  # noqa
from src.dependencies import (
    LojaServiceDependency,
    PedidoServiceDependency
)


router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.get("/")
async def requisitar_pedidos(
    service: PedidoServiceDependency,
    loja_uuid: Optional[str] = Query(None),
    usuario_uuid: Optional[str] = Query(None),
    limit: int = Query(0),
    offset: int = Query(1),
) -> Pedidos:

    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid
    if usuario_uuid is not None:
        kwargs["usuario_uuid"] = usuario_uuid

    pedidos_itens = await service.get_all_pedidos(**kwargs)
    paginate = Paginador(pedidos_itens, offset, limit)
    return Pedidos(**paginate.get_response())


@router.get("/{uuid}")
async def requisitar_pedido(
    service: PedidoServiceDependency,
    uuid: Annotated[str, Path(title="O uuid do pedido a fazer get")]
) -> PedidoGET:

    pedido = await service.get_pedido(uuid)
    if pedido is None or pedido.uuid is None:
        raise NotFoundException("Pedido não encontrado")

    return pedido


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_pedidos(
    service: PedidoServiceDependency,
    pedido_data: PedidoPOST,
) -> dict:

    try:
        await service.save_pedido(pedido_data=pedido_data)
        return {}
    except Exception as error:

        import traceback
        traceback.print_exc()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Erro no cadastro do pedido! detail: {error}'
        )


@router.patch("/alterar_status_de_pedido/{uuid}")
async def alterar_status_de_pedido(
    service: PedidoServiceDependency,
    loja: LojaServiceDependency,
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
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Erro no cadastro do pedido! detail: {error}'
        )


@router.patch("/concluir_pedido/{uuid}")
async def concluir_pedido(
    service: PedidoServiceDependency,
    loja: LojaServiceDependency,
    uuid: Annotated[str, Path(title="O uuid do pedido a fazer patch")],
):

    try:
        await service.concluir_pedido(pedido_uuid=uuid)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as error:
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Erro no cadastro do pedido! detail: {error}'
        )


@router.delete("/{uuid}")
async def remover_pedido(
    service: PedidoServiceDependency,
    loja: LojaServiceDependency,
    uuid: Annotated[str, Path(title="O uuid do pedido a fazer delete")]
):

    try:
        await service.remover_pedido(uuid=uuid)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
