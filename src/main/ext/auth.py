from flask_login import LoginManager
from flask import Flask, url_for, redirect, request
from src.infra.database import entities as e
from src.infra.database import repository as r


def init_app(app: Flask) -> None:

    login_manager = LoginManager()
    login_manager.init_app(app=app)

    @login_manager.user_loader
    def get_user(user_uuid) -> e.User:
        user = r.User.find_one(uuid=user_uuid)
        if user:
            return user
        
    @login_manager.unauthorized_handler
    def unauthorized():
        next = request.url
        return redirect(url_for('auth.login'), next=next)
