import flask
from .settings import main_project
import home

home.home_page.add_url_rule(
    rule= "/",
    view_func= home.render_home,
    methods = ["GET" ,"POST"]
)
main_project.register_blueprint(blueprint= home.home_page)