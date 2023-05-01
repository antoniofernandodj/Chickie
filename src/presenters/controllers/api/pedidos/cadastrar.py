from src.data.schema import PedidoDados, ItemDePedidoDados
from src.presenters.models.http import HTTPResponse
from src import data

def handle(dados: dict):

    items_payload = dados['items']
    pedido_payload = dados['pedido']

    pedido_dados = PedidoDados.parse_obj(obj=pedido_payload)
    response_data = data.pedido.cadastrar_pedido(dados=pedido_dados)

    items_payload['pedido_uuid'] = response_data['uuid']

    items_dados = ItemDePedidoDados.parse_obj(items_payload)
    response_data = data.pedido.cadastrar_item_de_pedido(dados=items_dados)

    response = HTTPResponse()

    return response