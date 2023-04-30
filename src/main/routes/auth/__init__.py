from src.presenters import controllers
from flask import (Blueprint, render_template, redirect,
                   flash, request)


bp = Blueprint('auth', __name__)

@bp.get('/login/')
def login_get():
    return render_template('auth/login.html')

@bp.post('/login/')
def login_post():
    form = request.form.to_dict()
    response = controllers.user.auth.login.handle(data=form)
    flash(message=response['message'], category=response['status'])
    if response['redirect']:
        return redirect(response['redirect'])

    return redirect('/login/')

@bp.get('/signin/')
def signin_get():
    return render_template('auth/signin.html')

@bp.post('/signin/')
def sign_post():
    form = request.form.to_dict()
    response = controllers.user.auth.signin.handle(data=form)
    flash(message=response['message'], category=response['status'])
    if response['redirect']:
        return redirect(response['redirect'])

    return redirect('/signin/')
