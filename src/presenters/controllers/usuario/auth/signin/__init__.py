from src.infra.database.repository import UsuarioRepository
from src.infra.database import entities as e
from src.presenters.models.http import HTTPResponse

def handle(data: dict):
    password1 = data['password1']
    password2 = data['password2']

    user_email = UsuarioRepository.find_one(email=data['email'])
    user_username = UsuarioRepository.find_one(username=data['username'])
    user_tel = UsuarioRepository.find_one(telefone=data['tel'])
    user_cel = UsuarioRepository.find_one(celular=data['cel'])

    user = user_email or user_username or user_tel or user_cel

    if password1 != password2:
        response = HTTPResponse(
            status='error',
            status_code=400,
            message=f'The passwords are different',
            redirect=None
        )

        return response

    if user:
        response = HTTPResponse(
            status='error',
            status_code=400,
            message=f'Invalid credentials! Use another.',
            redirect=None
        )

        return response

    user = UsuarioRepository.create(
        nome=data['name'],
        email=data['email'],
        password_hash=data['password1'],
        username=data['username'],
        telefone=data['tel'],
        celular=data['cel']
    )

    response = HTTPResponse(
        status='success',
        status_code=200,
        message=f'User {user.nome} registered successfuly',
        redirect='/home/'
    )

    return response