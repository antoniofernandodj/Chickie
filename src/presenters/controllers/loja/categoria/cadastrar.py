from src.infra.database import repository as r
from src.infra.database import entities as e
from src.presenters.models.http import HTTPResponse
from uuid import uuid4


def handle(data: dict):

    loja = r.Loja.find_one(email=data['uuid'])
    
    if loja is None:
        response = HTTPResponse(
            message='',
            status='',
            redirect='',
        )

        return response

    categoria = e.Categoria(
        uuid = uuid4(),
        nome = data['nome'],
        descricao = data['descricao'],
        imagem = data['imagem']
    )

    categoria.save()

    response = HTTPResponse(
        message='',
        status='',
        redirect='',
    )

    return response