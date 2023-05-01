from src.infra.database import repository as r
from src.infra.database import entities as e
from src.presenters.models.http import HTTPResponse

def handle(dados: dict):

    categoria = r.CategoriaRepository.find_one(dados['categoria_uuid'])
    if categoria:
        r.CategoriaRepository.update_one(categoria, dados['data'])

    return HTTPResponse(status='success', message='Item atualizado com sucesso!')
