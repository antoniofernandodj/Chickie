from src.presenters import controllers
from . import pedidos, precos, produtos, categorias
from flask import (Blueprint, render_template, redirect,
                   flash, request)


bp = Blueprint('api', __name__, url_prefix='/api/')


bp.register_blueprint(blueprint=pedidos.bp)
bp.register_blueprint(blueprint=precos.bp)
bp.register_blueprint(blueprint=produtos.bp)
bp.register_blueprint(blueprint=categorias.bp)
