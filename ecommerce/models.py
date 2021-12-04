from tools.database import db
from datetime import datetime as d


class UserInformation(db.Model):
    """ For Payments it's necessary UserInformation for users or not. """
    __tablename__ = 'users_information'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True, unique=True, default=None)
    name = db.Column(db.String(10),nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    province = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    street = db.Column(db.String(20), nullable=False)
    additional = db.Column(db.String(100), default='')
    postal_code = db.Column(db.String(10), unique=False, nullable=False)
    dni = db.Column(db.String(8), nullable=False)
    cart = db.Column(db.PickleType, nullable=False, default=[])
    favorites = db.Column(db.PickleType, nullable=False, default=[])
    history = db.Column(db.PickleType, nullable=False, default=[])


class Category(db.Model):
    """ It's necessary a Category, when is created is asigned of a product. """
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True)
    visible = db.Column(db.Boolean, index=True, default=False)


class Product(db.Model):
    """ Products for cart. """
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    photo_list = db.Column(db.PickleType, nullable=True)
    category = db.Column(db.PickleType, nullable=False)
    stock = db.Column(db.Integer, index=True, unique=False)
    name = db.Column(db.String(50), index=True, unique=False)
    information = db.Column(db.String(500), index=True, unique=False)
    url = db.Column(db.String(200), index=True, unique=True)
    price = db.Column(db.Integer, index=True, unique=False)
    visible = db.Column(db.Boolean, index=True, unique=False, default=False)


class Payment(db.Model):
    """ Used for payment and record. """
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True, unique=False, default=None)
    user_information = db.Column(db.Integer, index=True, unique=False)
    products = db.Column(db.PickleType)
    price = db.Column(db.Float, index=True, unique=False)
    datetime = db.Column(db.DateTime,index=True,unique=False,default=d.utcnow)
    status = db.Column(db.Integer, index=True, unique=False)

