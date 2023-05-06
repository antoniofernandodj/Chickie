from flask import Blueprint
from . import auth, home


bp = Blueprint('usuario', __name__)

bp.register_blueprint(auth.bp)
bp.register_blueprint(home.bp)
