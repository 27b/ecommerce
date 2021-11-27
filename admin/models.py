from tools.database import db

class Setting(db.Model):
    """ Used for configure admin proccess. """
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    value = db.Column(db.String(50), nullable=False, default=None)

