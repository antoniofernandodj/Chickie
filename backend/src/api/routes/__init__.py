from fastapi import FastAPI
from . import resources, auth
import tomli

# Read the version from pyproject.toml
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
        return {
            "version": version,
            "name": name,
            "description": description,
            "links": [
                {"rel": "self", "href": "https://api.example.com/"},
            ]
            + [
                {"rel": route.path.split("/")[1], "href": route.path}
                for route in app.router.routes
                if route.path != "/"
            ],
            "actions": [
                {
                    "name": route.name.replace("_", " ").capitalize(),
                    "methods": list(route.methods),
                    "path": route.path,
                }
                for route in app.router.routes
            ],
        }

    @app.get("/favicon.ico")
    async def favicon():
        return b""
