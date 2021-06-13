from flask import Blueprint, render_template, url_for, request, flash, redirect
from .models import User
from werkzeug.security import check_password_hash, generate_password_hash
from src import db
from flask_login import login_user, logout_user, login_required


accounts = Blueprint('accounts', __name__)

@accounts.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            #comparing the 2 hashes if matche
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('accounts.index'))
            
            else:
                flash('password is incorrect', category='error')
        else:
            flash('that user doesnt exist', category='error')

    return render_template('auth/login.html')


@accounts.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        #getting data from html form
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        check_user = User.query.filter_by(email=email).first()

        #basic verification if everything checks
        if check_user:
            flash('Email already in use', category='error')
        elif len(email) < 10 or len(first_name) < 3 or len(last_name) < 3:
            flash('size to short', category='error')
        elif password1 != password2:
            flash('Passwords dont match', category='error')
        else:
            #creating new user after everything checks out
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('User was created', category='success')
            return redirect(url_for('accounts.login'))

    return render_template('auth/register.html')


@accounts.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('accounts.login'))


@accounts.route('/main-page', methods=['GET'])
def index():
    return render_template('auth/main.html')
