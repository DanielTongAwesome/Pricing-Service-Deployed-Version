'''
    author: Zitian(Daniel) Tong
    date: 09:05 2019-05-19 2019
    editor: PyCharm    
    email: danieltongubc@gmail.com 
'''

from flask import request, render_template, Blueprint, redirect, url_for, session
from Pricing_Service.models.alert import Alert
from Pricing_Service.models.item import Item
from Pricing_Service.models.store import Store
from Pricing_Service.models.user import requires_login

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
@requires_login
def index():
    alerts = Alert.find_many_by('user_email', session['email'])
    return render_template('alerts/index.html', alerts=alerts)


@alert_blueprint.route('/new', methods=['GET', 'POST'])
@requires_login
def create_alert():
    if request.method == 'POST':

        # get from the front form
        alert_name = request.form['name']
        item_url = request.form['item_url']
        price_limit = float(request.form['price_limit'])

        # from form info find store info, tag_name, and query info
        store = Store.find_by_url(item_url)
        item = Item(item_url, store.tag_name, store.query)
        item.load_price()
        item.save_to_mongo()

        Alert(alert_name, item._id, price_limit, session['email']).save_to_mongo()

    return render_template('alerts/new_alert.html')


@alert_blueprint.route('/edit/<string:alert_id>', methods=['GET', 'POST'])
@requires_login
def edit_alerts(alert_id):
    alert = Alert.find_by_id(alert_id)

    if request.method == 'POST':
        edit_price_limit = float(request.form['price_limit'])

        alert.price_limit = edit_price_limit
        alert.save_to_mongo()

        return redirect(url_for('.index'))

    return render_template('alerts/edit_alerts.html', alert=alert)


@alert_blueprint.route('/delete/<string:alert_id>')
@requires_login
def delete_alerts(alert_id):
    alert = Alert.find_by_id(alert_id)
    if alert.user_email == session['email']:
        alert.remove_from_mongo()
    return redirect(url_for('.index'))
