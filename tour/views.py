import flask
from main.settings import DATABASE
from flask_login import current_user
from .models import Ticket

tour_id = 0

def render_tours():
    global tour_id
    if flask.request.method == 'POST':
        tour_id = flask.request.form["button"]
        print(tour_id)
        return flask.redirect('/tour/')
    #     tickets = Ticket(title = "Ticket to Paris", date = "10.11.2024", Country = "France", price = int(10000), descriprion = "BUY IT PLESE😭😭😭")
    #     DATABASE.session.add(tickets)
    #     DATABASE.session.commit()
    try:
        username = current_user.username
    except Exception as e:
        print(e)
        username = "1"
    return flask.render_template(
        "tours.html", tickets = Ticket.query.all(),
        is_auth = current_user.is_authenticated,
        username = username
        )
def render_tour():
    global tour_id
    try:
        username = current_user.username
    except Exception as e:
        print(e)
        username = "1"
    return flask.render_template(
        "tour.html",
        is_auth = current_user.is_authenticated,
        username = username
        )
