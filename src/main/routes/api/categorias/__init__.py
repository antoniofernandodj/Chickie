from src.presenters import controllers
from flask import (Blueprint, render_template, redirect,
                   flash, request)


bp = Blueprint('categorias', __name__, url_prefix='/categorias/')


@bp.get('/')
def requisitar_categorias():
    data = request.form.to_dict()
    response = controllers.api.categorias.requisitar_todos.handle(data=data)
    return response


@bp.get('/<string:uuid>')
def requisitar_categoria():
    data = request.form.to_dict()
    response = controllers.api.categorias.requisitar_um.handle(data=data)
    return response


@bp.post('/')
def cadastrar_categorias():
    data = request.form.to_dict()
    response = controllers.api.categorias.cadastrar.handle(data=data)
    return response


@bp.patch('/<string:uuid>')
def atualizar_categoria():
    data = request.form.to_dict()
    response = controllers.api.categorias.atualizar.handle(data=data),
    return response


@bp.delete('/<string:uuid>')
def remover_categoria():
    data = request.form.to_dict()
    response = controllers.api.categorias.remover.handle(data=data)
    return response

