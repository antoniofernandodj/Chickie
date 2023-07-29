from src.infra.database import repositories as r
from src.infra.database import entities as e
from src.presenters.models.http import HTTPResponse


def handle(data: dict):

    r.CategoriaRepository.remove_one(uuid=data['loja_uuid'])
    
    return HTTPResponse()
