from src.infra.database_postgres import DSN
from src.infra.database_postgres.handlers import CommandHandler
from src.domain.models import CategoriaProdutos
import aiopg
import psycopg2
import pytest


LOJA_UUID = '2196ed4a-a43c-4ff6-aecd-56da06e03004'


async def test_command_handler():
    async with aiopg.create_pool(DSN) as pool:
        async with pool.acquire() as connection:

            cmd_handler = CommandHandler(connection)

            categoria1 = CategoriaProdutos(
                nome='cat1', descricao='desc',
                loja_uuid=LOJA_UUID
            )

            categoria2 = CategoriaProdutos(
                nome='cat2', descricao='desc',
                loja_uuid=LOJA_UUID
            )

            categoria3 = CategoriaProdutos(
                nome='cat3', descricao='desc',
                loja_uuid=''  # raises HERE!
            )

            cmd_handler.save([categoria1, categoria2, categoria3])

            assert len(cmd_handler.commands) == 3

            results = []
            with pytest.raises(psycopg2.errors.ForeignKeyViolation):
                result = await cmd_handler.commit()
                results.extend(result)

            assert len(results) == 0
