from src.infra.database.repository import UsuarioRepository
from src.infra.cache import get_cache
from src.lib.auth import classes as c
from src.lib.auth import erros as e
from src.lib import security
from datetime import datetime, timedelta
from config import settings as s
from flask import request
from contextlib import suppress
import functools
import json


def get_id(user):
    _id, _uuid = None, None
    with suppress(AttributeError):
        _id = user.id

    with suppress(AttributeError):
        _uuid = user.uuid

    id = _uuid or _id
    if id is None:
        raise e.LoginException('Nenhum id disponível')
    
    return id


def login_data(request):

    cache = get_cache()
    login_cookie_crypt = request.cookies.get(f'x-usr')
    if login_cookie_crypt is None:
        return None

    user_id = security.descriptografar(login_cookie_crypt)
    login_key = f'login.user.{user_id}'

    login_value_crypt = cache[login_key]
    if login_value_crypt is None:
        return None 
    
    login_value_json = security.descriptografar(login_value_crypt)
    user_data = json.loads(login_value_json)

    return user_data   


def current_user(request):

    user_data = login_data(request)
    if user_data is None:
        return None

    user_dict = user_data['user']
    usuario = UsuarioRepository.find_one(uuid=user_dict['uuid'])

    return usuario


def login_user(user, expire_time=1800):
    cache = get_cache()
    
    id = get_id(user)
    
    user_data = user.__dict__
    user_data.pop('_sa_instance_state', None)

    login_key = f'login.user.{id}'
    login_value = json.dumps({
        'user': user_data,
        'time': datetime.utcnow().isoformat(sep='T'),
        'expire_time': expire_time,
    })

    login_value_crypt = security.criptografar(login_value)

    cache[login_key] = login_value_crypt
    print('Login realizado com sucesso!')

    return c.LoginData(user=user, max_age=expire_time)


def logout_user(user):
    cache = get_cache()

    _id = None
    _uuid = None
    try:
        _id = user.id
    except:
        pass

    try:
        _uuid = user.uuid
    except:
        pass

    id = _uuid or _id
    if id is None:
        raise e.LoginException('Nenhum id disponível')
    
    login_key = f'login.user.{id}'
    cache.delete(login_key)
    print('logout realizado com sucesso!')


def login_required(f):
    from flask import redirect, flash

    functools.wraps(f)
    def decorator(*a, **kw):
        data = login_data(request)
        if data is None:
            response = redirect(s.LOGIN_URL)
            return response

        login_time = datetime.fromisoformat(data['time'])
        expire_time: datetime = data['expire_time']
        expire_td = timedelta(seconds=expire_time)

        now = datetime.utcnow()
        if now > login_time + expire_td:
            response = redirect(s.LOGIN_URL)
            return response
        
        remaining_time = login_time + expire_td - now
        if remaining_time <= timedelta(minutes=1):
            flash('', category='session')
        
        usuario = current_user(request)
        if usuario:
            response = f(*a, **kw)

        else:
            response = redirect(s.LOGIN_URL)

        return response
    
    return decorator
