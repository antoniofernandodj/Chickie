from src.presenters import controllers
from flask import (Blueprint, render_template, redirect,
                   flash, request)

bp = Blueprint('api', __name__, url_prefix='/api/')
