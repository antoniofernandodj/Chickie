from src.presenters import controllers
from flask import (Blueprint, render_template, redirect,
                   flash, request)


bp = Blueprint('content', __name__)

@bp.get('/home/')
def home_get():
    return render_template('content/home.html')
