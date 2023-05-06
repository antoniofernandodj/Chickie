from src.lib import auth
from src.presenters import controllers
from flask import (Blueprint, render_template, make_response)


bp = Blueprint('home', __name__)

@bp.get('/home/')
@auth.login_required
def home():
    
    pagina = render_template('usuario/home.html')
    response = make_response(pagina)

    return response