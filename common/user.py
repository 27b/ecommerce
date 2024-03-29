from settings import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from common.datetime import datetime_generator as dtg


class User(db.Model, UserMixin):
    """ This model is used throughout the project. """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer, index=True, default=1)
    email = db.Column(db.String(50), index=True, unique=True)
    confirmed_email = db.Column(db.Boolean, default=False)
    pw_hash = db.Column(db.String(102), index=False)
    joined_at = db.Column(db.String(14), index=True, default=dtg.utcnow())

    def set_password(self, password: str) -> None:
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.pw_hash, password)

