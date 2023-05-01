from src.infra.database import repository as r
from src.infra.database import entities as e
from src.presenters.models.http import HTTPResponse

def handle(dados: dict):

    categoria = r.PrecoRepository.find_one(dados['categoria_uuid'])
    r.PrecoRepository.update_one(categoria, dados['data'])

    return HTTPResponse()
