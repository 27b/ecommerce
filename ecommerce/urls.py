from flask import Blueprint, render_template, redirect, url_for, abort, flash
from flask_login import login_user, logout_user, login_required, current_user
from ecommerce.forms import RegisterForm, LoginForm
from ecommerce.models import Category, Product
from user import User
from settings import db
#from tools.logger import logger


ecommerce = Blueprint('ecommerce', __name__, template_folder='templates')

# Routes for anonymous users
@ecommerce.route('/')
def home():
    products = Product.query.filter_by(visible=True)
    return render_template('views/home.html', products=products)


@ecommerce.route('/register/', methods=['GET', 'POST'])
def register():
    """ Create user account. """

    if current_user.is_authenticated:
        return redirect(url_for('ecommerce.user'))

    form = RegisterForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        email_in_db = User.query.filter_by(email=email).first()

        if not email_in_db:
            new_user = User(email=email)
            new_user.set_password = password
            db.session.add(new_user)
            db.session.commit()

            #logger.info(f'New user: {new_user.email}')

            return redirect(url_for('ecommerce.login'))

        flash('Email already in use.', 'info')

    return render_template('views/register.html', form=form)


@ecommerce.route('/login', methods=['GET', 'POST'])
def login():
    """ Send and get form with data, validate the data and login user. """

    if current_user.is_authenticated:
        return redirect(url_for('ecommerce.user'))

    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user_in_db = User.query.filter_by(email=email).first()

        # Validate user values
        if user_in_db and user_in_db.check_password(password):
            login_user(user)
            return redirect(url_for('ecommerce.user'))

        # If not user in db
        flash('Email already in use.', 'info')

    return render_template('login.html', form=form)


@ecommerce.route('/lost-password/', methods=['GET', 'POST'])
def lost_password():
    """ Send email to user. """
    pass


@ecommerce.route('/category/<category_name>/')
def category(category_name):
    """ Get all product of an specific category. """
    # Check if category exists.
    category = Category.query.filter_by(name=category_name).first()

    # Get visible products of category
    products = Product.query \
                      .filter_by(category=category.name, visible=True) \
                      .all()

    return render_template('index.html', products=products)


@ecommerce.route('/product/<product_url>/')
def product(product_url):
    """ Get specific product (only if it's visible). """
    product = Product.query.filter_by(product_url=product_url).first()

    if product and product.visible:
        return render_template('product.html', product=product)

    return redirect(url_for('index'))


# Routes for logged users
@ecommerce.route('/me/', methods=['GET'])
@login_required
def user():
    """ Get user data. """
    return render_template('views/user.html')


@ecommerce.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('ecommerce.index'))

