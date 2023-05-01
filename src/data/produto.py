from src.infra.database import entities as e
from uuid import uuid4


def cadastrar(data: dict) -> dict:

    produto = e.Produto(
        uuid = uuid4(),
        nome = data['nome'],
        descricao = data['descricao'],
        categoria = data['categoria'],
        imagem = data['imagem'],
        loja = data['loja']
    )

    produto.save()

    response = {
        'message': '',
        'status': '',
        'status_code': '',
        'redirect': '',
    }

    return response