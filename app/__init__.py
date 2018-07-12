from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

# Authentication
login = LoginManager(app)
login.session_protection = 'strong'
login.login_view = 'login'
login.init_app(app)

db = SQLAlchemy(app)

from app.functions import init_log
log = init_log('flavor')

from views import main








