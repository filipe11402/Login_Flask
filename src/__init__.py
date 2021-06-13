from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'login.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdasd'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .auth import views

    app.register_blueprint(views.accounts, url_prefix='/accounts')

    from .auth.models import User

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'accounts.login'

    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(user_id)


    create_database(app)

    return app


def create_database(app):
    if not path.exists('src/' + DB_NAME):
        db.create_all(app=app)