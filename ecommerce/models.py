from common.database import db
from datetime import datetime as d


class UserInformation(db.Model):
    """ For Payments it's necessary UserInformation for users or not. """
    __tablename__ = 'users_information'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True, unique=True, default=None)
    name = db.Column(db.String(10), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    province = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    street = db.Column(db.String(20), nullable=False)
    additional = db.Column(db.String(100), nullable=True)
    postal_code = db.Column(db.String(10), nullable=False)
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
    images = db.Column(db.PickleType, nullable=False)
    category = db.Column(db.String, nullable=False)
    stock = db.Column(db.Integer, index=True)
    name = db.Column(db.String(50), index=True, unique=True)
    information = db.Column(db.String(500), index=False)
    url = db.Column(db.String(200), index=True, unique=True)
    price = db.Column(db.Integer, index=True)
    visible = db.Column(db.Boolean, index=True, default=False)
    deleted = db.Column(db.Boolean, index=True, default=False)


class Payment(db.Model):
    """ Used for payment and record. """
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True, default=None)
    user_information = db.Column(db.Integer, index=True)
    products = db.Column(db.PickleType)
    price = db.Column(db.Float, index=True)
    datetime = db.Column(db.DateTime, index=True, default=d.utcnow)
    status = db.Column(db.Boolean, index=True, default=False)


class Order(db.Model):
    """ Status of payment for admins. """
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(64), nullable=False)
    note = db.Column(db.String(256), nullable=True)
    
