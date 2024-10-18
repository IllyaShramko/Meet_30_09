import flask, flask_sqlalchemy, flask_migrate

main_project = flask.Flask(
    import_name= "main",
    template_folder= "templates"
)
main_project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app= main_project)

migrate = flask_migrate.Migrate(app= main_project, db= DATABASE)