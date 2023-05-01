from src.presenters import controllers
from flask import (Blueprint, render_template, redirect,
                   flash, request)


bp = Blueprint('pedidos', __name__, url_prefix='/pedidos/')


@bp.get('/')
def requisitar_pedidos():
    data = request.form.to_dict()
    response = controllers.pedidos.requisitar_todos.handle(data=data)
    return response


@bp.get('/<string:uuid>')
def requisitar_pedido():
    data = request.form.to_dict()
    response = controllers.pedidos.requisitar_um.handle(data=data)
    return response


@bp.post('/')
def cadastrar_pedidos():
    data = request.form.to_dict()
    response = controllers.pedidos.cadastrar.handle(data=data)
    return response


@bp.patch('/<string:uuid>')
def atualizar_pedido():

    data = request.form.to_dict()
    ACTION_HANDLERS = {
        "entregar": controllers.pedidos.entregar.handle,
        "concluir": controllers.pedidos.concluir.handle,
    }

    action = request.headers.get('x-acao')
    if action in ACTION_HANDLERS:
        return ACTION_HANDLERS[action](data)

    return {}, 400


@bp.delete('/<string:uuid>')
def remover_pedidos():
    data = request.form.to_dict()
    response = controllers.pedidos.cadastrar.handle(data=data)
    return response

