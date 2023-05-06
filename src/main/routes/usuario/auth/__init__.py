from src.presenters import controllers
from config import settings as s
from src.lib import auth
from src.lib import security
from flask import (Blueprint, render_template, redirect,
                   flash, request, make_response)


bp = Blueprint('auth', __name__)


@bp.get('/login/')
def login_get():
    return render_template('/auth/login.html')

@bp.post('/login/')
def login_post():
    
    form = request.form.to_dict()
    login_data, response = controllers.usuario.auth.login.handle(data=form)
    flash(message=response.message, category=response.status)
    
    if response.redirect and login_data is not None:
        user_data = security.criptografar(login_data.user.uuid)
        response = redirect(response.redirect)
        print({'login_data.max_age': login_data.max_age})
        response.set_cookie(
            'x-usr', user_data,
            path='/', max_age=login_data.max_age
        )

        return response

    return redirect('/login/')

@bp.get('/renew/')
def renew():
    user = auth.current_user(request)
    login_data = auth.login_user(user, expire_time=s.SESSION_TIME)
    response = make_response(redirect(request.referrer or '/home/'))
    user_data = security.criptografar(login_data.user.uuid)
    response.set_cookie(
        'x-usr', user_data,
        path='/', max_age=login_data.max_age
    )
    return response

@bp.get('/signin/')
def signin_get():
    return render_template('/auth/signin.html')

@bp.post('/signin/')
def sign_post():
    form = request.form.to_dict()
    response = controllers.usuario.auth.signin.handle(data=form)
    flash(message=response.message, category=response.status)
    if response.redirect:
        return redirect(response.redirect)

    return redirect('/signin/')

@bp.get('/logout/')
def logout():
    user = auth.current_user(request)
    auth.logout_user(user)
    return redirect('/login/')
