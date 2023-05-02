from uuid import uuid4
from datetime import datetime
from src.presenters.models.http import HTTPResponse
from src.infra.database import entities as e

def handle(payload: dict):

    pedido_payload = payload['pedido']
    itens_payload = payload['items']

    if not isinstance(pedido_payload, dict):
        response = HTTPResponse()
        return response
    
    if not isinstance(itens_payload, list):
        response = HTTPResponse
        return response

    pedido_uuid = uuid4()

    pedido = e.Pedido(
        uuid = pedido_uuid,
        data_hora = datetime.utcnow(),
        status = pedido_payload['status'],
        frete = pedido_payload['frete'],
        endereco = pedido_payload['endereco'],
        loja = pedido_payload['loja']
    )

    pedido.save()

    for item_payload in itens_payload:
        item = e.ItemPedido(
            uuid = uuid4(),
            quantidade = item_payload['quantidade'],
            subtotal = item_payload['subtotal'],
            produto_uuid = item_payload['produto'],
            pedido_uuid = pedido_uuid,
            loja_uuid = item_payload['loja']
        )

        item.save()

    response = HTTPResponse()
    return response
