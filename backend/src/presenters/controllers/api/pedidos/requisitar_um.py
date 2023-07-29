from src.presenters.models.http import HTTPResponse
from src.infra.database import repositories as r


def handle(data: dict):

    pedido = r.PedidoRepository.find_one(uuid=data['uuid'])
    if pedido:
        return HTTPResponse(body=pedido.dict())
    
    return HTTPResponse()
