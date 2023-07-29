from fastapi import APIRouter
from . import (
    pedidos,
    precos,
    produtos,
    categorias
)


router = APIRouter(prefix='')


router.include_router(pedidos.router)
router.include_router(precos.router)
router.include_router(produtos.router)
router.include_router(categorias.router)
