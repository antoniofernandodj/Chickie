from src.infra.database import repository as r
from src.infra.database import entities as e

def handle(data: dict):
    password1 = data['password1']
    password2 = data['password2']

    if password1 != password2:
        response = {
            'status': 'error',
            'status_code': 400,
            'message': f'The passwords are different',
            'redirect': None
        }

        return response

    if r.User.find_one(email=data['email']):
        response = {
            'status': 'error',
            'status_code': 400,
            'message': f'Invalid credentials! Use another.',
            'redirect': None
        }

        return response

    user = r.User.create(
        name=data['name'],
        email=data['email'],
        password_hash=data['password1'],
    )

    response = {
        'status': 'success',
        'status_code': 200,
        'message': f'User {user.name} registered successfuly',
        'redirect': '/home/'
    }

    return response