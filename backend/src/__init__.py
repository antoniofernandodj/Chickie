from fastapi import FastAPI
from contextlib import suppress
import asyncio
import warnings

warnings.filterwarnings(
    "ignore",
    category=RuntimeWarning,
    message="coroutine 'init_app' was never awaited",
)


def create_app(args: list) -> FastAPI:
    app = FastAPI()

    from src.api import routes
    from src.api import ext

    routes.init_app(app)
    ext.config.init_app(app)
    ext.middlewares.init_app(app)
    ext.logging.init_app(app)

    with suppress(RuntimeError):
        asyncio.run(ext.init_commands.init_app())

    return app
