from copy import copy
from src.presenters import controllers
from flask import Blueprint, request


bp = Blueprint('produtos', __name__, url_prefix='/produtos/')


@bp.get('/')
def requisitar_produtos():
    data = copy(request.json)
    response = controllers.api.produtos.requisitar_todos.handle(data=data)
    return response


@bp.get('/<string:uuid>')
def requisitar_produto(uuid):
    data = copy(request.json)
    data['uuid'] = uuid
    response = controllers.api.produtos.requisitar_um.handle(data=data)
    return response


@bp.post('/')
def cadastrar_produtos():
    data = copy(request.json)
    response = controllers.api.produtos.cadastrar.handle(data=data)
    return response


@bp.patch('/<string:uuid>')
def atualizar_produto(uuid):
    data = copy(request.json)
    data['uuid'] = uuid
    response = controllers.api.produtos.atualizar.handle(data=data),
    return response


@bp.delete('/<string:uuid>')
def remover_produto(uuid):
    data = copy(request.json)
    data['uuid'] = uuid
    response = controllers.api.produtos.remover.handle(data=data)
    return response
