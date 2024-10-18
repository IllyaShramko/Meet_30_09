import flask
from flask_login import current_user
from main.settings import DATABASE
from main.flask_config import mail
import flask_mail

def render_home():
    if flask.request.method == "POST":
        try:
            text_message = f'Клієнт {flask.request.form["client_name"]} залишив(-ла) відгук:\n\n{flask.request.form["message"]}:\n\n{flask.request.form["client_email"]}'
            print("e")
            print(flask.request)
            text_message1 = flask_mail.Message(
                subject = "Відгук від клієнта",
                body = text_message,
                recipients = ["123illya123123r@gmail.com"],
                sender= flask.request.form["client_email"]
            )
            print("1")
            mail.send(text_message1)
            print("2")
        except Exception as e:
            print(e)
    try:
        username = current_user.username
    except Exception as e:
        print(e)
        username = "1"
    return flask.render_template("home.html",
        is_auth = current_user.is_authenticated,
        username = username
        )
    
        