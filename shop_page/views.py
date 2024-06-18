import flask
from .models import Product

def show_shop():
    return flask.render_template('shop.html', products = Product.query.all())