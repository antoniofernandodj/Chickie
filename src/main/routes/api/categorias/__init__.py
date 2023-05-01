from src.presenters import controllers
from flask import (Blueprint, render_template, redirect,
                   flash, request)


bp = Blueprint('categorias', __name__, url_prefix='/categorias/')


@bp.get('/')
def requisitar_categorias():
    data = request.json
    response = controllers.api.categorias.requisitar_todos.handle(data=data)
    return response.to_flask()


@bp.get('/<string:uuid>')
def requisitar_categoria():
    data = request.json
    response = controllers.api.categorias.requisitar_um.handle(data=data)
    return response.to_flask()


@bp.post('/')
def cadastrar_categorias():
    data = request.json
    response = controllers.api.categorias.cadastrar.handle(data=data)
    return response.to_flask()


@bp.patch('/<string:uuid>')
def atualizar_categoria():
    data = request.json
    response = controllers.api.categorias.atualizar.handle(data=data),
    return response.to_flask()


@bp.delete('/<string:uuid>')
def remover_categoria():
    data = request.json
    response = controllers.api.categorias.remover.handle(data=data)
    return response.to_flask()

