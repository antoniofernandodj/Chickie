from src.presenters import controllers
from flask import (Blueprint, render_template, redirect,
                   flash, request)


bp = Blueprint('home', __name__)


@bp.get('/loja/')
def home():
    return render_template('/loja/home.html')


@bp.get('/loja/historico/')
def historico():
    return render_template('/loja/historico.html')


@bp.get('/loja/categorias/')
def historico():
    return render_template('/loja/categorias.html')


@bp.get('/loja/produtos/')
def historico():
    return render_template('/loja/produtos.html')


@bp.get('/loja/pedidos/')
def cadastrar_pedidos_get():
    return render_template('/loja/pedidos.html')


@bp.get('/loja/clientes/')
def cadastrar_pedidos_get():
    return render_template('/loja/clientes.html')


@bp.get('/loja/dados/')
def cadastrar_pedidos_get():
    return render_template('/loja/dados.html')
