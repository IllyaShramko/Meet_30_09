
import flask
from .settings import main_project
import home, tour, user

home.home_page.add_url_rule(
    rule= "/",
    view_func= home.render_home,
    methods= ["GET", "POST"]
)
main_project.register_blueprint(blueprint= home.home_page)

user.user_app.add_url_rule(
    rule= "/registration/",
    view_func= user.render_registration,
    methods= ["GET", "POST"]
)
user.user_app.add_url_rule(
    rule= "/login/",
    view_func= user.render_login,
    methods= ["GET", "POST"]
)
main_project.register_blueprint(blueprint= user.user_app)

tour.tour_app.add_url_rule(
    rule = "/tour/",
    view_func = tour.render_tour,
    methods = ["GET", "POST"]
)
tour.tour_app.add_url_rule(
    rule = "/tours/",
    view_func = tour.render_tours,
    methods = ["GET", "POST"]
)
main_project.register_blueprint(blueprint= tour.tour_app)
