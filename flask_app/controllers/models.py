from flask_app import app, render_template, session, redirect, request
import requests
from flask_app.models.item import Item
from flask_app.models.order import Order
from pprint import pprint


# @app.route("/dashboard")
# def dashbaord():
#     if 'user_id' in session:
#         return render_template('dashboard.html')
#     return redirect('/')


@app.route("/store")
def store():
    if 'user_id' in session:
        data = Item.get_all()
        status_check = {'status': 'process'}
        if Order.get_process_order(status_check):
            session['order_id'] = Order.get_process_order(status_check)
        else:
            data = { 'user_id': session['user_id'], 'status': 'process'}
            session['order_id'] = Order.add(data)
        return render_template('store.html', data=data)
    return redirect('/signin')

@app.route("/iteminfo/<int:id>")
def item_info(id):
    if 'user_id' in session:
        id_dict = {'id': id}
        data = Item.get_one(id_dict)
        print(data)
        return render_template('iteminfo.html', data=data)
    return redirect('/signin')


@app.route("/cart")
def cart():
    if 'user_id' in session:
        order_id = {'order_id': session['order_id']}
        data = Order.get_by_id(order_id)
        pprint(data)
        return render_template('cart.html', data=data)
    return redirect('/signin')


@app.route("/additem/<int:id>")
def add_item(id, ):
    data = {
        'order_id': session['order_id'],
        'item_id': id
    }
    Order.order_add_items(data)
    return redirect('/store')



@app.route("/checkout")
def checkout():
    if 'user_id' in session:
        order_id = {'order_id': session['order_id']}
        data = Order.get_by_id(order_id)
        return render_template('checkout.html', data=data)
    return redirect('/signin')