import flask_login
from .settings import main_project
from user.models import User

main_project.secret_key = "key"

login_manager = flask_login.LoginManager(app= main_project)
login_manager.init_app(app= main_project)
@login_manager.user_loader
def load_user(id):
    return User.query.get(ident= id)