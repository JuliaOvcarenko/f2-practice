import flask

cart_app = flask.Blueprint(
    name = 'Cart',
    import_name = 'cart_page',
    template_folder = 'templates'
)