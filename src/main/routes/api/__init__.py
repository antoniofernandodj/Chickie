from flask import Blueprint
from . import (
    pedidos,
    precos,
    produtos,
    categorias
)


bp = Blueprint('api', __name__, url_prefix='/api/')


bp.register_blueprint(blueprint=pedidos.bp)
bp.register_blueprint(blueprint=precos.bp)
bp.register_blueprint(blueprint=produtos.bp)
bp.register_blueprint(blueprint=categorias.bp)
