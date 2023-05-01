from src.data.schema import PedidoDados, ItemDePedidoDados
from src.presenters.models.http import HTTPResponse
from src.infra.database import repository as r
from src import data

def handle(data: dict):

    produto = r.ProdutoRepository.find_one(data['produto_uuid'])

    return HTTPResponse(body=produto.dict())
