from flask_login import login_user
from src.infra.database import repository as r
from src.presenters.models.http import HTTPResponse

from werkzeug.security import (
    check_password_hash as check_hash,
)


def handle(data: dict):
    user = r.User.find_one(email=data['email'])

    remember_value = data.get('rememberMe')
    remember = bool(int(remember_value) if remember_value else 0)

    if not user:

        response = HTTPResponse(message='Invalid credentials!',
                                status='error', redirect='/user/login/')

        return response
    
    valid_credentials = check_hash(user.password_hash, data['password'])
    
    if not valid_credentials:
        response = HTTPResponse(message='Invalid credentials!',
                                status='error', redirect='/user/login/')
        return response
    
    user.id = user.uuid
    login_user(user, remember=remember)

    response = HTTPResponse(status='success', redirect='/user/home/',
                message='Logged in successfuly!')

    return response