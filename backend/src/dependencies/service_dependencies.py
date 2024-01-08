from .connection_dependency import connection_dependency
from typing import Annotated
from fastapi import Depends
from src.services import (
    ProdutoService,
    PedidoService,
    AvaliacaoDeLojaService,
    LojaService
)


async def get_produto_service(connection: connection_dependency):
    return ProdutoService(connection=connection)


async def get_loja_service(connection: connection_dependency):
    return LojaService(connection=connection)


async def get_pedido_service(connection: connection_dependency):
    return PedidoService(connection=connection)


async def get_avaliacao_de_loja_service(connection: connection_dependency):
    return AvaliacaoDeLojaService(connection=connection)


avaliacao_de_loja_service_dependency = Annotated[
    AvaliacaoDeLojaService,
    Depends(get_avaliacao_de_loja_service)
]

produto_service_dependency = Annotated[
    ProdutoService,
    Depends(get_produto_service)
]

loja_service_dependency = Annotated[
    LojaService,
    Depends(get_loja_service)
]

pedido_service_dependency = Annotated[
    PedidoService,
    Depends(get_pedido_service)
]
