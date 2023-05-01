from flask_login import login_user, login_url
from src.infra.database import repository as r
from src.presenters.models.http import HTTPResponse

from werkzeug.security import (
    check_password_hash as check_hash,
)


def handle(data: dict):
    loja = r.Loja.find_one(email=data['email'])

    remember_value = data.get('rememberMe')
    remember = bool(int(remember_value) if remember_value else 0)

    if not loja:
        response = HTTPResponse(message='Invalid credentials!',
                            status='error', redirect='/loja/login/')
        return response
    
    valid_credentials = check_hash(loja.password_hash, data['password'])
    
    if not valid_credentials:
        response = HTTPResponse(message='Invalid credentials!',
                            status='error', redirect='/loja/login/')
        return response
    
    loja.id = loja.uuid
    login_user(loja, remember=remember)

    response = HTTPResponse(status='success', redirect='/loja/home/',
                            message='Logged in successfuly!')

    return response