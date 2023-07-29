from src.presenters.models.http import HTTPResponse
from src.infra.database import repositories as r
from src import data


def handle(data: dict):

    loja_uuid = data.get('loja_uuid')
    if loja_uuid:
        produtos = r.ProdutoRepository.find_all(loja_uuid=loja_uuid)
        return HTTPResponse(body=produtos)
    
    return HTTPResponse()
