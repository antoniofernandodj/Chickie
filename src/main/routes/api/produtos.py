from copy import copy
from src.presenters import controllers
from fastapi import APIRouter


router = APIRouter(
    prefix='/produtos',
    tags=["Produtos"]
)


@router.get('/')
def requisitar_produtos():
    # data = copy(request.json)
    # response = controllers.api.produtos.requisitar_todos.handle(data=data)
    # return response
    return {}


@router.get('/<string:uuid>')
def requisitar_produto(uuid):
    # data = copy(request.json)
    # data['uuid'] = uuid
    # response = controllers.api.produtos.requisitar_um.handle(data=data)
    # return response
    return {}


@router.post('/')
def cadastrar_produtos():
    # data = copy(request.json)
    # response = controllers.api.produtos.cadastrar.handle(data=data)
    # return response
    return {}


@router.patch('/<string:uuid>')
def atualizar_produto(uuid):
    # data = copy(request.json)
    # data['uuid'] = uuid
    # response = controllers.api.produtos.atualizar.handle(data=data),
    # return response
    return {}



@router.put('/<string:uuid>')
def atualizar_produto_2(uuid):
    # data = copy(request.json)
    # data['uuid'] = uuid
    # response = controllers.api.produtos.atualizar.handle(data=data),
    # return response
    return {}


@router.delete('/<string:uuid>')
def remover_produto(uuid):
    # data = copy(request.json)
    # data['uuid'] = uuid
    # response = controllers.api.produtos.remover.handle(data=data)
    # return response
    return {}
