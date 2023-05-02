from src.infra.database import repository as r
from src.infra.database import entities as e
from src.presenters.models.http import HTTPResponse

def handle(dados: dict):

    preco = r.PrecoRepository.find_one(uuid=dados['uuid'])
    if preco:
        r.PrecoRepository.update_one(preco, dados['data'])

    return HTTPResponse()
