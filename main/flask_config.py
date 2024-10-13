import flask_mail
from .settings import main_project

main_project.config["MAIL_SERVER"] = "smtp.gmail.com"
main_project.config["PORT"] = 587
main_project.config["MAIL_USE_TLS"] = True
main_project.config["MAIL_USERNAME"] = "artemvaschenko83@gmail.com"
main_project.config["MAIL_PASSWORD"] = "sncj nczy toqt atlm"

mail = flask_mail.Mail(main_project)