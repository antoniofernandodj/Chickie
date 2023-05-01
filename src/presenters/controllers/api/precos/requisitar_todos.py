from src.data.schema import PedidoDados, ItemDePedidoDados
from src.presenters.models.http import HTTPResponse
from src.infra.database import repository as r
from src import data

def handle(data: dict):

    preco = r.PrecoRepository.find_one(data['preco_uuid'])

    return HTTPResponse(body=preco.dict())
