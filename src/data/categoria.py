from src.infra.database import entities as e
from datetime import datetime
from uuid import uuid4



def cadastrar(data: dict) -> dict:

    categoria = e.Categoria(
        uuid = uuid4(),
        nome = data['nome'],
        descricao = data['descricao'],
        imagem = data['imagem']
    )

    categoria.save()

    response = {
        'message': '',
        'status': '',
        'status_code': '',
        'redirect': '',
    }

    return response