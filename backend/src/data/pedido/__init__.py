
from src.infra.database import entities as e
from src.data.schema import PedidoDados, ItemDePedidoDados
from datetime import datetime
from uuid import uuid4


def cadastrar_pedido(dados: PedidoDados) -> dict:

    uuid = uuid4()

    pedido = e.Pedido(
        uuid = uuid,
        dados_hora = datetime.utcnow(),
        status = dados.status,
        frete = dados.frete,
        endereco = dados.endereco,
        loja = dados.loja_uuid
    )

    pedido.save()

    response = {
        'message': '',
        'status': '',
        'uuid': uuid
    }

    return response

def cadastrar_item_de_pedido(dados: ItemDePedidoDados):

    item = e.ItemPedido(
        uuid = uuid4(),
        quantidade = dados.quantidade,
        subtotal = dados.subtotal,
        produto_uuid = dados.produto_uuid,
        pedido_uuid = dados.pedido_uuid,
        loja_uuid = dados.loja_uuid
    )

    item.save()

    response = {
        'message': '',
        'status': ''
    }

    return response
