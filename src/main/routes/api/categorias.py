# from src.presenters import controllers
from fastapi import APIRouter
from src.schemas import Categoria


router = APIRouter(
    prefix='/categorias',
    tags=["Categorias"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@router.get('/')
def requisitar_categorias():
    # data = copy(request.json)
    # response = controllers.api.categorias.requisitar_todos.handle(data=data)
    # return response.to_fastapi()
    return {}


@router.get('/<string:uuid>')
def requisitar_categoria(uuid):
    # data = copy(request.json)
    # data['uuid'] = uuid
    # response = controllers.api.categorias.requisitar_um.handle(data=data)
    # return response.to_fastapi()
    return {}


@router.post('/')
def cadastrar_categorias(categoria: Categoria):
    # data = copy(request.json)
    # response = controllers.api.categorias.cadastrar.handle(data=data)
    # return response.to_fastapi()
    return {}


@router.patch('/<string:uuid>')
def atualizar_categoria():
    # data = copy(request.json)
    # data['uuid'] = uuid
    # response = controllers.api.categorias.atualizar.handle(data=data),
    # return response.to_fastapi()
    return {}


@router.put('/<string:uuid>')
def atualizar_categoria_2():
    # data = copy(request.json)
    # data['uuid'] = uuid
    # response = controllers.api.categorias.atualizar.handle(data=data),
    # return response.to_fastapi()
    return {}



@router.delete('/<string:uuid>')
def remover_categoria(uuid):
    # data = copy(request.json)
    # data['uuid'] = uuid
    # response = controllers.api.categorias.remover.handle(data=data)
    # return response.to_fastapi()
    return {}
