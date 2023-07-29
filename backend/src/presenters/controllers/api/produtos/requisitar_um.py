from src.presenters.models.http import HTTPResponse
from src.infra.database import repositories as r


def handle(data: dict):

    produto = r.ProdutoRepository.find_one(uuid=data['uuid'])
    if produto:
        return HTTPResponse(body=produto.dict())
    
    return HTTPResponse()
