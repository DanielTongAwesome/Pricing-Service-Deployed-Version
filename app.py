'''
    author: Zitian(Daniel) Tong
    date: 15:33 2019-05-03 2019
    editor: PyCharm    
    email: danieltongubc@gmail.com 
'''

import os
from flask import Flask, render_template
from Pricing_Service.views.alerts import alert_blueprint
from Pricing_Service.views.stores import store_blueprint
from Pricing_Service.views.users import user_blueprint

app = Flask(__name__)
app.secret_key = os.urandom(64)  # randomly generate 64 characters to protect the session
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)


@app.route('/')
def home():
    return render_template('home.html')


app.register_blueprint(alert_blueprint, url_prefix='/alerts')
app.register_blueprint(store_blueprint, url_prefix='/stores')
app.register_blueprint(user_blueprint, url_prefix='/users')


if __name__ == '__main__':
    app.run(debug=True)