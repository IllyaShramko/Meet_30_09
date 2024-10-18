import flask_mail
from .settings import main_project

main_project.config["MAIL_SERVER"] = "smtp.gmail.com"
main_project.config["MAIL_PORT"] = 587
main_project.config["MAIL_USE_TLS"] = True
main_project.config["MAIL_USERNAME"] = "123illya123123r@gmail.com"
main_project.config["MAIL_PASSWORD"] = "yshv yhmu lozm faji"

mail = flask_mail.Mail(main_project)