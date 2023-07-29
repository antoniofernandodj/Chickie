from src.presenters.models.http import HTTPResponse
from src.infra.database import repositories as r


def handle(data: dict):

    preco = r.PrecoRepository.find_one(uuid=data['uuid'])
    if preco:
        return HTTPResponse(body=preco.dict())
    
    return HTTPResponse()
