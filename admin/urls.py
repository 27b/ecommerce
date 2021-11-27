from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
#from tools.logger import logger

admin = Blueprint('admin', __name__, template_folder='templates')

def check_admin():
    if current_user.role != 2:
        #logger.info(f'{current_user.email} enter in admin route')
        return redirect(url_for('ecommerce.home'))


@admin.route('/')
@login_required
def index():
    return render_template('views/index.html')


@admin.route('/products/', methods=['GET', 'POST'])
@login_required
def products():
    """ Load a list of products and allow add new products """
    check_admin()

    return render_template('views/products.html')


@admin.route('/products/<product_url>/<action>', methods=['GET', 'POST'])
@login_required
def products_product(product_url, action):
    """ Edit, update and delete products """
    check_admin()


@admin.route('/categories/')
@login_required
def categories():
    check_admin()


@admin.route('/orders/')
@login_required
def orders():
    check_admin()


@admin.route('/files/')
@login_required
def files():
    check_admin()


@admin.route('users')
@login_required
def users():
    check_admin()

