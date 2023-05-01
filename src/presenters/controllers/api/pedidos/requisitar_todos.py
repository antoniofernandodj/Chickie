from src.presenters.models.http import HTTPResponse
from src.infra.database import repository as r
from src import data

def handle(data: dict):

    pedidos = r.PedidoRepository.find_all(loja_uuid=data['loja_uuid'])

    return HTTPResponse(body=pedidos)
