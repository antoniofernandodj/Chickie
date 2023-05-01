from src.presenters import controllers
from flask import (Blueprint, render_template, redirect,
                   flash, request)


bp = Blueprint('home', __name__)

@bp.get('/loja/')
def home():
    return render_template('/loja/home.html')

@bp.get('/loja/historico/')
def historico():
    return render_template('/loja/home.html')

@bp.get('/loja/pedidos/')
def cadastrar_pedidos_get():
    return render_template('/loja/home.html')
