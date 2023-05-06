from src.lib import auth
from src.infra.database.repository import UsuarioRepository
from src.presenters.models.http import HTTPResponse
from config import settings as s

from werkzeug.security import (
    check_password_hash as check_hash,
)


def handle(data: dict):
    
    user_email = UsuarioRepository.find_one(email=data['login'])
    user_username = UsuarioRepository.find_one(username=data['login'])
    user_tel = UsuarioRepository.find_one(telefone=data['login'])
    user_cel = UsuarioRepository.find_one(celular=data['login'])

    user = user_email or user_username or user_tel or user_cel

    remember_value = data.get('rememberMe')
    remember = bool(int(remember_value) if remember_value else 0)

    if not user:
        response = HTTPResponse(
            message='Invalid credentials!',
            status='error',
            redirect='/login/'
        )

        return None, response
    
    valid_credentials = check_hash(
        pwhash=user.password_hash,
        password=data['password']
    )
    
    if not valid_credentials:
        response = HTTPResponse(
            message='Invalid credentials!',
            status='error',
            redirect='/login/'
        )

        return None, response
    
    user.id = user.uuid
    expire_time = s.SESSION_TIME
    login_data = auth.login_user(
        user=user, expire_time=expire_time
    )

    response = HTTPResponse(
        status='success',
        redirect='/home/',
        message='Logged in successfuly!'
    )

    return login_data, response