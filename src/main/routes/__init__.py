from fastapi import FastAPI
from . import (
    api,
    auth
)


def init_app(app: FastAPI) -> None:
    # app.include_router(api.router)
    app.include_router(auth.router)
