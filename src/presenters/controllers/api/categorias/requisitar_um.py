from src.presenters.models.http import HTTPResponse
from src.infra.database import repository as r


def handle(data: dict):

    categoria = r.CategoriaRepository.find_one(uuid=data['uuid'])
    if categoria:
        return HTTPResponse(body=categoria.dict())
    
    return HTTPResponse()
