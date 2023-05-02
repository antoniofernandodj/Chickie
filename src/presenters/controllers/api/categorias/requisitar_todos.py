from src.presenters.models.http import HTTPResponse
from src.infra.database import repository as r


def handle(data: dict):

    loja_uuid = data.get('loja_uuid')
    if loja_uuid:
        categorias = r.CategoriaRepository.find_all(loja_uuid=loja_uuid)
        return HTTPResponse(body=categorias)

    return HTTPResponse()
