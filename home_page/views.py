import flask

def show_home():
    return flask.render_template('home.html')