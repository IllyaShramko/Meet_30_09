from .settings import main_project
import tour

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