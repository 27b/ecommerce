from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from admin.forms import ProductForm
#from tools.logger import logger


admin = Blueprint('admin',__name__, template_folder='templates',
        static_folder='static')

def check_admin():
    if current_user.role != 2:
        #logger.info(f'{current_user.email} enter in admin route')
        return redirect(url_for('ecommerce.home'))


@admin.route('/')
@login_required
def index():
    """ Dashboard. """
    check_admin()
    return render_template('views/index.html')

@admin.route('/products/', methods=['GET', 'POST'])
@login_required
def products():
    """ Load a list of products. """
    check_admin()
    return render_template('views/products.html', title=None)


@admin.route('/products/new-product')
def new_product():
    """ Create new product. """
    check_admin()
    form = ProductForm()
    return render_template('views/products.html', form=form, action='add')

@admin.route('/products/<product_url>/<action>', methods=['GET', 'POST'])
@login_required
def products_product(product_url, action):
    """ Edit, update and delete products. """
    check_admin()
    pass

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

