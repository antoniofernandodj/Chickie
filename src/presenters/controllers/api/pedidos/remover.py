from src.data.schema import PedidoDados, ItemDePedidoDados
from src.presenters.models.http import HTTPResponse
from src.infra.database import repository as r
from src import data

def handle(data: dict):

    r.PedidoRepository.remove_one(uuid=data['pedido_uuid'])

    return HTTPResponse()
