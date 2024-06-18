import flask
from shop_page.models import Product
from project.settings import DATABASE

def show_cart():
    if flask.request.method == "POST":
        new_product = Product(
            name = flask.request.form["name"],
            description = flask.request.form["description"],
            price = flask.request.form["price"],
            count = flask.request.form["count"]
        )
        DATABASE.session.add(new_product)
        DATABASE.session.commit()
    return flask.render_template('cart.html')