from fastapi import APIRouter
from . import (  # noqa
    avaliacoes_de_lojas,
    pedidos,
    precos,
    produtos,
    categorias,
    avaliacoes_de_produtos,
    entregadores,
    funcionarios,
    metodos_de_pagamento,
    pagamentos,
    zona_de_entrega,
    status,
)

router = APIRouter(prefix="")

router.include_router(pedidos.router)
router.include_router(precos.router)
router.include_router(produtos.router)
router.include_router(categorias.router)
# router.include_router(entregadores.router)
# router.include_router(avaliacoes_de_lojas.router)
# router.include_router(avaliacoes_de_produtos.router)
# router.include_router(funcionarios.router)
# router.include_router(metodos_de_pagamento.router)
# router.include_router(pagamentos.router)
# router.include_router(zona_de_entrega.router)
router.include_router(status.router)
