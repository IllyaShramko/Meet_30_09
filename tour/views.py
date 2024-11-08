import flask
from main.settings import DATABASE
from flask_login import current_user
from .models import Ticket
# 
tour_id = 0
ticket_choosen = False
def render_tours():
    global tour_id, ticket_choosen
    if flask.request.method == 'POST':
        tour_id = flask.request.form["button"]
        ticket_choosen = True

        print(tour_id)
        # tickets = Ticket(
        #     title = "Ticket to visit Sun",
        #     date = "01.09.2077", 
        #     Country = "Great Britan",
        #     price = 35999999,
        #     descriprion = "IT`S HOT😡👹 AND SOOOO COLDDD 🤯🥶🦐 BUT YOU CAN BUY GRILL FOR 20 BILLIONS")
        # DATABASE.session.add(tickets)
        # DATABASE.session.commit()
        return flask.redirect('/tour/')
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
    global tour_id, ticket_choosen
    try:
        username = current_user.username
    except Exception as e:
        print(e)
        username = "1"
    return flask.render_template(
        "tour.html",
        is_auth = current_user.is_authenticated,
        username = username,
        ticket_choosen = ticket_choosen,
        ticket = Ticket.query.filter_by(id = tour_id)
        )
