import flask
from main.settings import DATABASE
from main.flask_config import mail
import flask_mail

def render_home():
    try:
        text_message = f'Клієнт {flask.request.form["client_name"]} залишив(-ла) відгук:\n\n{flask.request.form["message"]}:\n\n{flask.request.form["client_email"]}'
        text_message1 = flask_mail.Message(
            subject = "Відгук від клієнта",
            body = text_message,
            recipients = ["123illya123123r@gmail.com"],
            sender = flask.request.form["client_email"]
        )
        mail.send(text_message1)
    except:
        print("")
    return flask.render_template("home.html")
    
        