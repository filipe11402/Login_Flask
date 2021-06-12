from flask import Blueprint, render_template, url_for, request
from .models import User

accounts = Blueprint('accounts', __name__)

@accounts.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        print("EMAIL: {}".format(email))

    return render_template('auth/login.html')
@accounts.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html')
