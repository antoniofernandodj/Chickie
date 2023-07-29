from src.infra.database import entities as e
from src.infra.database.repositories import UsuarioRepository
from src.data.schema import UsuarioDados


def cadastrar(dados: UsuarioDados) -> dict:

    usuario = UsuarioRepository.find_one(nome=dados.nome)

    if usuario is not None:
        response = {
            'message': f'Usuario com nome {dados.nome} já cadastrado!',
            'status': 'error'
        }

        return response
    
    if dados.password1 != dados.password2:
        response = {
            'message': f'As senhas digitadas são diferentes!',
            'status': 'error'
        }

        return response
    
    usuario = UsuarioRepository.create(
        nome = dados.nome,
        username = dados.username,
        email = dados.email,
        telefone = dados.telefone,
        celular = dados.celular,
        password_hash = dados.password2
    )

    response = {
        'message': f'Usuario criado com sucesso!',
        'status': 'error',
        'uuid': usuario.uuid
    }

    return response
