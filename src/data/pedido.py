from src.infra.database import entities as e
from datetime import datetime
from uuid import uuid4


def cadastrar(data: dict) -> dict:

    pedido = e.Pedido(
        uuid = uuid4(),
        data_hora = datetime.utcnow(),
        status = data['status'],
        frete = data['frete'],
        endereco = data['endereco'],
        loja = data['loja']
    )

    pedido.save()

    response = {
        'message': '',
        'status': '',
        'status_code': '',
        'redirect': '',
    }

    return response