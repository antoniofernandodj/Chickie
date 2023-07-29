from src.infra.database import repositories as r
from src.infra.database import entities as e
from src.presenters.models.http import HTTPResponse
from src import data
from src.data.schema import PrecoDados

def handle(dados: dict):

    preco_dados = PrecoDados.parse_obj(dados)
    result = data.preco.cadastrar(dados=preco_dados)

    return HTTPResponse()
