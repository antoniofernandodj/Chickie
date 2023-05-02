from copy import copy
from src.presenters import controllers
from flask import Blueprint, request


bp = Blueprint('precos', __name__, url_prefix='/precos/')


@bp.get('/')
def requisitar_precos():
    data = copy(request.json)
    response = controllers.api.precos.requisitar_todos.handle(data=data)
    return response


@bp.get('/<string:uuid>')
def requisitar_preco(uuid):
    data = copy(request.json)
    data['uuid'] = uuid
    response = controllers.api.precos.requisitar_um.handle(data=data)
    return response


@bp.post('/')
def cadastrar_precos():
    data = copy(request.json)
    response = controllers.api.precos.cadastrar.handle(data=data)
    return response


@bp.patch('/<string:uuid>')
def atualizar_preco(uuid):
    data = copy(request.json)
    data['uuid'] = uuid
    response = controllers.api.precos.atualizar.handle(data=data),
    return response


@bp.delete('/<string:uuid>')
def remover_preco(uuid):
    data = copy(request.json)
    data['uuid'] = uuid
    response = controllers.api.precos.remover.handle(data=data)
    return response

