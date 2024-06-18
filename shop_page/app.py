import flask

shop_app = flask.Blueprint(
    name = 'Shop',
    import_name = 'shop_page',
    template_folder = 'templates'
)