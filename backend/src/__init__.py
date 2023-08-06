from fastapi import FastAPI


def create_app(args: list) -> FastAPI:
    app = FastAPI()

    from src.main import routes
    from src.main import ext

    routes.init_app(app)
    ext.config.init_app(app)
    ext.middlewares.init_app(app)

    return app
