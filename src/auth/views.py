from flask import Blueprint

accounts = Blueprint('accounts', __name__)

@accounts.route('/')
def index():
    return '<h1>HELLO WORLD</h1>'