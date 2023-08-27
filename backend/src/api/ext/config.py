from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def init_app(app: FastAPI):

    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Chickie",
        version="0.1.0",
        description="App de entrega de refeições",
        routes=app.routes
    )
    app.openapi_schema = openapi_schema
