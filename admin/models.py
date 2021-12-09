from tools.database import db
from tools.datetime_format import datetime_generator as dtg


class Setting(db.Model):
    """ Used for configure admin proccess. """
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    value = db.Column(db.String(50), nullable=False, default=None)


class Notification(db.Model):
    """ Global notifications in admin panel. """
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    information = db.Column(db.String(256), nullable=False)
    link = db.Column(db.String(512), nullable=True, default="#NotLink")
    datetime = db.Column(db.String(14), index=True, default=dtg.utcnow())

