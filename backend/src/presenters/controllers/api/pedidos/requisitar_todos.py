from src.presenters.models.http import HTTPResponse
from src.infra.database import repositories as r


def handle(data: dict):

    loja_uuid = data.get('loja_uuid')
    if loja_uuid:
        pedidos = r.PedidoRepository.find_all(loja_uuid=data['loja_uuid'])
        return HTTPResponse(body=pedidos)
    
    return HTTPResponse()
