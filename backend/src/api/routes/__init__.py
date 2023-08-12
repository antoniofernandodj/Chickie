from fastapi import FastAPI
from . import resources, auth


def init_app(app: FastAPI) -> None:
    app.include_router(auth.usuario.router)
    app.include_router(auth.loja.router)
    app.include_router(resources.router)
