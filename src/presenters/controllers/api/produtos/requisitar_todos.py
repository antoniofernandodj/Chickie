from src.data.schema import PedidoDados, ItemDePedidoDados
from src.presenters.models.http import HTTPResponse
from src.infra.database import repository as r
from src import data

def handle(data: dict):

    produtos = r.ProdutoRepository.find_all(data['empresa_uuid'])

    return HTTPResponse(body=produtos)
