from flask_app import app, render_template, session, redirect
import requests
from flask_app.models.item import Item


@app.route("/dashboard")
def dashbaord():
    data = requests.get("https://fakestoreapi.com/products").json()
    print(data)
    for item in data:
        Item.save(item)
    if 'user_id' in session:
        return render_template('dashboard.html', data=data)
    return redirect('/')


@app.route("/store")
def store():
    if 'user_id' in session:
        return render_template('store.html')
    return redirect('/dashboard')

@app.route("/cart")
def cart():
    if 'user_id' in session:
        return render_template('cart.html')
    return redirect('/dashboard')

@app.route("/checkout")
def checkout():
    if 'user_id' in session:
        return render_template('checkout.html')
    return redirect('/dashboard')