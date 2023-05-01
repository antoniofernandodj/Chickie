from src.presenters import controllers
from flask import (Blueprint, render_template, redirect,
                   flash, request)


bp = Blueprint('auth', __name__)


@bp.get('/loja/login/')
def login_get():
    return render_template('/loja/login.html')


@bp.post('/loja/login/')
def login_post():
    form = request.form.to_dict()
    response = controllers.usuario.auth.login.handle(data=form)
    flash(message=response['message'], category=response['status'])
    return redirect(response['redirect'])


@bp.get('/loja/signin/')
def signin_get():
    return render_template('/loja/signin.html')


@bp.post('/loja/signin/')
def sign_post():
    form = request.form.to_dict()
    response = controllers.usuario.auth.signin.handle(data=form)
    flash(message=response['message'], category=response['status'])
    return redirect('/signin/')
