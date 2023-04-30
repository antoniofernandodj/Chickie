from flask_login import login_user, login_url
from src.infra.database import repository as r

def handle(data: dict):
    user = r.User.find_one(email=data['email'])

    remember_value = data.get('rememberMe')
    remember = bool(int(remember_value) if remember_value else 0)

    if not user:
        response = {
            'message': 'Invalid credentials!',
            'status': 'error',
            'status_code': 404,
            'redirect': None
        }
        return response
    
    valid_credentials = r.User.validate_credentials(user, data['password'])
    if not valid_credentials:
        response = {
            'message': 'Invalid credentials!',
            'status': 'error',
            'status_code': 401,
            'redirect': None
        }
        return response
    
    user.id = user.uuid
    login_user(user, remember=remember)
    response = {
        'message': 'Logged in successfuly!',
        'status': 'success',
        'status_code': 200,
        'redirect': '/home/'
    }

    return response