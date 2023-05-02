from src.infra.database import repository as r
from src.infra.database import entities as e
from src.presenters.models.http import HTTPResponse

def handle(data: dict):
    password1 = data['password1']
    password2 = data['password2']

    if password1 != password2:

        response = HTTPResponse(status='error', redirect='/loja/signin/',
                     message=f'The passwords are different')

        return response

    if r.Loja.find_one(email=data['email']):

        response = HTTPResponse(status='error', redirect='/loja/signin/',
                     message=f'Invalid credentials! Use another.')

        return response

    loja = r.Loja.create(
        name=data['name'],
        email=data['email'],
        password_hash=data['password1'],
    )


    response = HTTPResponse(status='success', redirect='/loja/home/',
                message=f'Store {loja.nome} registered successfuly')

    return response
