from src.infra.database import repository as r
from src.infra.database import entities as e
from src.presenters.models.http import HTTPResponse
from src import data
from src.data.schema import ProdutoDados

def handle(dados: dict):

    produto_dados = ProdutoDados.parse_obj(dados)
    result = data.produto.cadastrar(dados=produto_dados)

    return HTTPResponse()
