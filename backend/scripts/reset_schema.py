import sys
import os
from pathlib import Path
import asyncio
from aiopg import create_pool
parent = str(Path(os.path.dirname(__file__)).parent)

sys.path.append(parent)

from src.infra.database_postgres import get_dsn  # type: ignore # noqa 


async def clear_database() -> None:

    sql = """
    delete from avaliacoes_de_loja;
    delete from avaliacoes_de_produtos;
    delete from clientes;
    delete from enderecos_lojas;
    delete from enderecos_usuarios;
    delete from entregadores;
    delete from funcionarios;
    delete from metodos_pagamento;
    delete from pagamentos;
    delete from zonas_de_entrega;
    delete from precos;
    delete from produtos;
    delete from categorias_de_produtos;
    delete from enderecos_entregas;
    delete from itens_pedido;
    delete from pedidos;
    delete from status;
    delete from lojas;
    delete from usuarios;
    """

    DSN = get_dsn(os.getenv('MODE'))

    async with create_pool(DSN) as pool:
        async with pool.acquire() as connection:
            async with connection.cursor() as cursor:
                cursor = await connection.cursor()
                await cursor.execute(sql)

asyncio.run(clear_database())
