import flask, os, flask_migrate, flask_sqlalchemy

project_flask = flask.Flask(
    import_name = 'project',
    template_folder = 'templates',
    instance_path = os.path.abspath(__file__ + '/..')
)
project_flask.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app = project_flask)
migrate = flask_migrate.Migrate(app = project_flask, db = DATABASE)