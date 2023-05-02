from src.infra.database import repository as r
from src.infra.database import entities as e
from src.presenters.models.http import HTTPResponse

def handle(dados: dict):

    produto = r.ProdutoRepository.find_one(uuid=dados['produto_uuid'])
    if produto:
        r.ProdutoRepository.update_one(produto, dados['data'])

    return HTTPResponse()
