from src.data.schema import PedidoDados, ItemDePedidoDados
from src.presenters.models.http import HTTPResponse
from src.infra.database import repositories as r
from src import data

def handle(data: dict):

    r.PedidoRepository.remove_one(uuid=data['uuid'])

    return HTTPResponse()
