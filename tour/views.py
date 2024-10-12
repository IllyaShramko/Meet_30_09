import flask
from main.settings import DATABASE
from .models import Ticket

def render_tours():
    if flask.request.method == 'POST':
        tickets = Ticket(title = "Ticket to Paris", date = "10.11.2024", Country = "France", price = int(10000), descriprion = "BUY IT PLESE😭😭😭")
        DATABASE.session.add(tickets)
        DATABASE.session.commit()
    return flask.render_template("tours.html", tickets = Ticket.query.all())
def render_tour():
    return flask.render_template("tour.html")
