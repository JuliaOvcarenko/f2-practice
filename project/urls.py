import home_page, cart_page, shop_page
from .settings import project_flask

home_page.home_app.add_url_rule(
    rule = '/',
    methods = ["GET", "POST"],
    view_func = home_page.show_home
)
project_flask.register_blueprint(blueprint = home_page.home_app)

cart_page.cart_app.add_url_rule(
    rule = '/cart/',
    methods = ["GET", "POST"],
    view_func = cart_page.show_cart
)
project_flask.register_blueprint(blueprint = cart_page.cart_app)

shop_page.shop_app.add_url_rule(
    rule = '/shop/',
    methods = ["GET", "POST"],
    view_func = shop_page.show_shop
)
project_flask.register_blueprint(blueprint = shop_page.shop_app)