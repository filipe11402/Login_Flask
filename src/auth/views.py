from flask import Blueprint, render_template, url_for
from .models import User

accounts = Blueprint('accounts', __name__)

@accounts.route('/login')
def login():
    return render_template('auth/login.html')