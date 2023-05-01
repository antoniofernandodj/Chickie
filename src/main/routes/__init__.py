from flask import Flask
from . import loja, usuario, api

def init_app(app: Flask) -> None:
    app.register_blueprint(loja.bp)
    app.register_blueprint(usuario.bp)
    app.register_blueprint(api.bp)