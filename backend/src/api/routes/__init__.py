from fastapi import FastAPI
from . import resources, auth
import tomli
import os

with open("pyproject.toml", "rb") as toml_file:
    toml_data = tomli.load(toml_file)
    version = toml_data["tool"]["poetry"]["version"]
    description = toml_data["tool"]["poetry"]["description"]
    name = toml_data["tool"]["poetry"]["name"]


def init_app(app: FastAPI) -> None:
    app.include_router(auth.usuario.router)
    app.include_router(auth.loja.router)
    app.include_router(resources.router)

    @app.get("/")
    async def index():
        """
        Rota para obter informações sobre o aplicativo e as rotas disponíveis.

        Retorna um JSON contendo informações sobre a versão, nome e descrição do aplicativo,
        bem como links para as rotas disponíveis e detalhes sobre as ações (rotas) do aplicativo.
        """
        return {
            "version": os.getenv('APP_VERSION'),
            "name": name,
            "description": description,
            "links": [
                {"rel": "self", "href": "http://localhost:8000/"},
            ]
            + [
                {
                    "rel": route.path.split("/")[1],  # type: ignore
                    "href": route.path,  # type: ignore
                }
                for route in app.router.routes
                if route.path != "/"  # type: ignore
            ],
            "actions": [
                {
                    "name": (
                        route.name.replace(  # type: ignore
                            "_", " "
                        ).capitalize()
                    ),
                    "methods": list(route.methods),  # type: ignore
                    "path": route.path,  # type: ignore
                }
                for route in app.router.routes  # type: ignore
            ],
        }

    @app.get("/favicon.ico")
    async def favicon():
        """
        Rota para servir o favicon do aplicativo.

        Retorna uma resposta vazia (b"").
        """
        return b""
