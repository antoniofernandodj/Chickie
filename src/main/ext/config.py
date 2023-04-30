from flask import Flask
from config import settings as s

from pathlib import Path
from os import path

def init_app(app: Flask):

    PROJECT_PATH = str(Path(__file__).parent.parent.parent.parent)

    TEMPLATE_FOLDER = path.join(
        PROJECT_PATH, 'src', 'main', 'templates'
    )
    STATIC_FOLDER = path.join(
        PROJECT_PATH, 'src', 'main', 'static'
    )

    app.template_folder = TEMPLATE_FOLDER
    app.static_folder = STATIC_FOLDER
    app.secret_key = s.FLASK_SECRET_KEY