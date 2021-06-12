from flask import Blueprint
from .models import User

accounts = Blueprint('accounts', __name__)

@accounts.route('/login')
def login():
    teste = User.query.all()
    print("AFSADASD: {}".format(teste))
    return '<h1>HELLO WORLD</h1>'