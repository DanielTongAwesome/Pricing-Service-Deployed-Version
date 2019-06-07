'''
    author: Zitian(Daniel) Tong
    date: 17:43 2019-05-25 2019
    editor: PyCharm    
    email: danieltongubc@gmail.com 
'''


from flask import Blueprint, render_template, request, url_for, redirect, session
from models.user import User, UserError

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.register_user(email, password):
                session['email'] = email
                return email

        except UserError as e:
            return e.message

    return render_template('users/register.html')   # send user an error if login was invalid


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email,password):
                session['email'] = email
                return redirect(url_for('alerts.index'))
        except UserError as e:
            return e.message

    return render_template('users/login.html')


@user_blueprint.route('/logout')
def logout_user():
    session['email'] = None
    return render_template('users/login.html')
