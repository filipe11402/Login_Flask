from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
DB_NAME = 'login.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdasd'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .auth import views

    create_database(app)

    app.register_blueprint(views.accounts, url_prefix='/accounts')

    return app


def create_database(app):
    if not os.path.exists('src/' + DB_NAME):
        db.create_all(app=app)
