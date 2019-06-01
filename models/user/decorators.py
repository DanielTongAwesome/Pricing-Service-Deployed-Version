'''
    author: Zitian(Daniel) Tong
    date: 18:00 2019-05-27 2019
    editor: PyCharm    
    email: danieltongubc@gmail.com 
'''

import functools
from typing import Callable
from flask import session, flash, redirect, url_for, current_app


def requires_login(f: callable) -> Callable:
    @functools.wraps(f)
    def decorated_functions(*args, **kwargs):
        if not session.get('email'):
            flash('You need to be signed in for this page', 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)
    return decorated_functions


def requires_admin(f:callable) -> callable:
    @functools.wraps(f)
    def decorated_functions(*args, **kwargs):
        if session.get('email') != current_app.config.get('ADMIN', ''):
            flash('You need to a administrator to access this page', 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)
    return decorated_functions
