from src.presenters import controllers
from flask import (Blueprint, render_template, redirect,
                   flash, request)


bp = Blueprint('auth', __name__)

@bp.get('/user/login/')
def login_get():
    return render_template('/user/auth/login.html')

@bp.post('/user/login/')
def login_post():
    form = request.form.to_dict()
    response = controllers.usuario.auth.login.handle(data=form)
    flash(message=response['message'], category=response['status'])
    if response['redirect']:
        return redirect(response['redirect'])

    return redirect('/user/login/')


@bp.get('/user/signin/')
def signin_get():
    return render_template('/user/auth/signin.html')

@bp.post('/user/signin/')
def sign_post():
    form = request.form.to_dict()
    response = controllers.usuario.auth.signin.handle(data=form)
    flash(message=response['message'], category=response['status'])
    if response['redirect']:
        return redirect(response['redirect'])

    return redirect('/user/signin/')
