import flask

home_app = flask.Blueprint(
    name = 'Home',
    import_name = 'home_page',
    template_folder = 'templates'
)