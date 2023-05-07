from flask import Flask
from werkzeug.security import generate_password_hash as gen_hash


class App(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, import_name=__name__, **kwargs)
        
        from src.infra import database
        from src.main import routes
        from src.main import ext
        
        database.config.init_database()
        ext.config.init_app(self)
        routes.init_app(self)
