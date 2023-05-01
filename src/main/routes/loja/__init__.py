from src.presenters import controllers
from flask import (Blueprint, render_template, redirect,
                   flash, request)


bp = Blueprint('loja', __name__)