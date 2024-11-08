import flask

home_page = flask.Blueprint(
    name = "home",
    import_name = "home",
    template_folder = "templates"
)