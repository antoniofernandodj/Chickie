from src.presenters import controllers
from flask import (Blueprint, render_template, redirect,
                   flash, request)


bp = Blueprint('precos', __name__, url_prefix='/precos/')


@bp.get('/')
def requisitar_precos():
    data = request.form.to_dict()
    response = controllers.api.precos.requisitar_todos.handle(data=data)
    return response


@bp.get('/<string:uuid>')
def requisitar_preco():
    data = request.form.to_dict()
    response = controllers.api.precos.requisitar_um.handle(data=data)
    return response


@bp.post('/')
def cadastrar_precos():
    data = request.form.to_dict()
    response = controllers.api.precos.cadastrar.handle(data=data)
    return response


@bp.patch('/<string:uuid>')
def atualizar_preco():
    data = request.form.to_dict()
    response = controllers.api.precos.atualizar.handle(data=data),
    return response


@bp.delete('/<string:uuid>')
def remover_preco():
    data = request.form.to_dict()
    response = controllers.api.precos.remover.handle(data=data)
    return response

