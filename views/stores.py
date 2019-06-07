'''
    author: Zitian(Daniel) Tong
    date: 16:52 2019-05-24 2019
    editor: PyCharm    
    email: danieltongubc@gmail.com 
'''

import json
from typing import Dict
from flask import Blueprint, render_template, request, url_for, redirect
from models.store import Store
from models.user.decorators import requires_admin, requires_login

store_blueprint = Blueprint('stores', __name__)


@store_blueprint.route('/')
@requires_login
def index():
    stores = Store.all()
    return render_template('stores/store_index.html', stores=stores)


@store_blueprint.route('/new', methods=['GET', 'POST'])
@requires_admin
def create_store():
    if request.method == 'POST':
        name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        query = request.form['query']

        Store(name, url_prefix, tag_name, query).save_to_mongo()

    return render_template('stores/new_store.html')


@store_blueprint.route('/edit/<string:store_id>', methods=['GET', 'POST'])
@requires_admin
def edit_stores(store_id):
    store = Store.find_by_id(store_id)

    if request.method == 'POST':
        edit_store_name = request.form['name']
        edit_store_url_prefix = request.form['url_prefix']
        edit_store_tag_name = request.form['tag_name']
        edit_store_query = request.form['query']

        store.name = edit_store_name
        store.url_prefix = edit_store_url_prefix
        store.tag_name = edit_store_tag_name

        # fix json and dict bug, no matter how user typed in, we all can convert it to Dict
        store.query = json.loads(edit_store_query)

        store.save_to_mongo()

        return redirect(url_for('.index'))

    return render_template('stores/edit_stores.html', store=store)


@store_blueprint.route('/delete/<string:store_id>')
@requires_admin
def delete_stores(store_id):
    store = Store.find_by_id(store_id).remove_from_mongo()
    return redirect(url_for('.index'))
