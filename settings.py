from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from dotenv import load_dotenv
from datetime import timedelta
from os import getenv


# APPLICACION INSTANCE
app = Flask(__name__, static_url_path="/")

# APPLICACION CONFIG
load_dotenv()
app.config['FLASK_ENV'] = getenv('FLASK_ENV')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=90)
app.config['TESTING'] = True
#app.config['DEBUG'] = True

# CSRF PROTECTION
csrf = CSRFProtect()
csrf.init_app(app)

# DATABASE CONFIG
db = SQLAlchemy()
db.init_app(app)

# Import database models
from user import *
from ecommerce.models import *
from admin.models import *

migrate = Migrate(app, db)

# LOGIN MANAGER
# Configure the behavior of sessions.
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

# Lgoin manager handlers
@login_manager.user_loader
def user_loader(user_id: int):
    return db.query('users').filter_by(id=user_id).first()

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('ecommerce.home'))


if __name__ == '__main__':
    """ Run "settings.py" for create database. """
    with app.app_context():
        db.drop_all()
        db.create_all(app=app)

