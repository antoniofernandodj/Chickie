from src.infra.database import repository as r
from src.infra.database import entities as e
from src.presenters.models.http import HTTPResponse


def handle(data: dict):

    categoria = r.CategoriaRepository.find_one(
        uuid=data['categoria_uuid']
    )

    if categoria:
        return HTTPResponse(body=categoria.dict())
    
    return HTTPResponse()
