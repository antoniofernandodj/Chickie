from src.data.schema import PedidoDados, ItemDePedidoDados
from src.presenters.models.http import HTTPResponse
from src.infra.database import repository as r
from src import data

def handle(data: dict):

    pedido = r.PedidoRepository.find_one(uuid=data['pedido_uuid'])
    if pedido:
        pedido.marcar_como_entregando()

    return HTTPResponse()
