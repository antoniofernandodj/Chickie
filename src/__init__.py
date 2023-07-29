from fastapi import FastAPI


def create_app() -> FastAPI:

    app = FastAPI()
    
    from src.main import routes
    from src.main import ext
    routes.init_app(app)
    return app