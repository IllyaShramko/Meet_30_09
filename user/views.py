import flask
from .models import User
from main.settings import DATABASE
import flask_login

def render_registration():
    confirmed = False
    if flask.request.method == 'POST':
        

        user = User(
            username = flask.request.form['username'],
            password = flask.request.form['password'],
        )
        try:
            DATABASE.session.add(user)
            DATABASE.session.commit()
            return flask.redirect("/login/")
        except:
            return "Не вдалося створити користувача"  
    print(confirmed)
    return flask.render_template(
        template_name_or_list='registration.html')
def render_login():
    return flask.render_template("login.html")