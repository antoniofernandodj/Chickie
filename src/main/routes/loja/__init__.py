from src.presenters import controllers
from flask import (Blueprint, render_template, redirect,
                   flash, request)

from src.main.routes.loja import (
    auth, home
)


bp = Blueprint('loja', __name__)

bp.register_blueprint(blueprint=auth.bp)
bp.register_blueprint(blueprint=home.bp)
