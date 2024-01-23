from config import settings as s  # noqa  # type: ignore
from src.infra.database_postgres import DSN  # type: ignore
from fastapi import FastAPI
from aiopg import create_pool, Pool, Connection
from src.misc import ConsoleColors as CC
import sys
import logging


def init_app(app: FastAPI):

    @app.on_event('startup')
    async def startup() -> None:

        async def on_pool_connect(connection: Connection):
            try:
                app.state.connections
            except AttributeError:
                app.state.connections = set()

            conn_id = str(id(connection))[-5:]
            msg = f'on_connect: Got connection ...{conn_id}'
            app.state.connections.add('...' + conn_id)
            logging.warning(CC.warning(msg))
            msg = CC.warning(str({'Connections': app.state.connections}))
            logging.warning(CC.warning(msg))

        try:
            pool = await create_pool(
                DSN, maxsize=1, minsize=1, echo=True
            )
            logging.warn('Cleaning connections...')
            pool.close()
            await pool.wait_closed()
            logging.warn('Connections cleaned.')

            app.state.connection_pool = await create_pool(
                DSN, maxsize=5, minsize=5,
                echo=True, on_connect=on_pool_connect
            )
        except Exception:
            try:
                pool = app.state.connection_pool
                pool.close()
                await pool.wait_closed()
            except Exception:
                pass

            sys.exit(1)

        app.state.connection_pool.echo
        print(f'Created pool {app.state.connection_pool}')

    @app.on_event('shutdown')
    async def shutdown() -> None:
        pool: Pool = app.state.connection_pool
        print(f'Got pool {pool}')
        pool.close()
        await pool.wait_closed()
        print('Finalizando...')
        print(f'Closed pool {pool}')
