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

    delete from ingredientes_item_pedido;    
    delete from avaliacoes_de_loja;
    delete from avaliacoes_de_produtos;
    delete from clientes;
    delete from enderecos_lojas;
    delete from enderecos_usuarios;
    delete from ingredientes;
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

    drop table ingredientes_item_pedido;
    drop table avaliacoes_de_loja;
    drop table avaliacoes_de_produtos;
    drop table clientes;
    drop table enderecos_lojas;
    drop table enderecos_usuarios;
    drop table ingredientes;
    drop table entregadores;
    drop table funcionarios;
    drop table pagamentos;
    drop table metodos_pagamento;
    drop table zonas_de_entrega;
    drop table precos;
    drop table produtos;
    drop table categorias_de_produtos;
    drop table enderecos_entregas;
    drop table itens_pedido;
    drop table pedidos;
    drop table status;
    drop table usuarios;
    drop table lojas;
    drop table alembic_version;

    DROP TYPE IF EXISTS uf CASCADE;
    DROP TYPE IF EXISTS dia_da_semana CASCADE;
    DROP TYPE IF EXISTS modo_de_cadastro CASCADE;
    """

    DSN = get_dsn(os.getenv('MODE'))

    async with create_pool(DSN) as pool:
        async with pool.acquire() as connection:
            async with connection.cursor() as cursor:
                cursor = await connection.cursor()
                await cursor.execute(sql)

asyncio.run(clear_database())
