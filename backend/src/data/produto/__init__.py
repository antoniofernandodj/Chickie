from src.infra.database import entities as e
from src.data.schema import ProdutoDados
from uuid import uuid4


def cadastrar(dados: ProdutoDados) -> dict:

    uuid = uuid4()

    produto = e.Produto(
        uuid = uuid,
        nome = dados.nome,
        descricao = dados.descricao,
        categoria = dados.categoria,
        loja = dados.loja_uuid
    )

    produto.save()

    response = {
        'message': '',
        'status': '',
        'uuid': uuid
    }

    return response
