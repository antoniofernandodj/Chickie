from src.infra.database import repository as r
from src.infra.database import entities as e
from src.presenters.models.http import HTTPResponse


def handle(data: dict):
    
    categorias = r.CategoriaRepository.find_all(loja_uuid=data['loja_uuid'])

    return HTTPResponse(body=categorias, status='success',
                        message='Categorias encontradas com sucesso')
