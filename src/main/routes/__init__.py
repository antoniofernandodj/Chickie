from flask import Flask
from . import auth
from . import content

def init_app(app: Flask) -> None:
    app.register_blueprint(auth.bp)
    app.register_blueprint(content.bp)