from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
)
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    """ Used in /register for auth. """
    email = StringField('Email', validators = [
        DataRequired(), Length(min=20, max=50)
    ])
    password = PasswordField('Password', validators = [
        DataRequired(), Length(min=8, max=50)
    ])
    password2 = PasswordField('Repeat password', validators = [
        DataRequired(), EqualTo('password')
    ])
    submit = SubmitField('Create account')


class LoginForm(FlaskForm):
    """ Used in /login for auth. """
    email = StringField('Email', validators = [
        DataRequired(), Length(min=5, max=35)
    ])
    password = PasswordField('Password', validators = [
        DataRequired(), Length(min=8, max=50)
    ])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign In')


class ProductForm(FlaskForm):
    """ Used in /admin-panel for add and edit products. """
    pass


class PaymentForm(FlaskForm):
    """ Used in /admin-panel for check and change status. """
    pass
