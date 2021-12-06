from flask import (
    current_app,
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
from flask_login import login_required, current_user
from admin.forms import ProductForm
from ecommerce.models import Product
from tools.database import db
from tools.tools import safe_url
from os import path
from uuid import uuid4
#from tools.logger import logger


admin = Blueprint('admin',__name__, template_folder='templates',
        static_folder='static')

@admin.before_request
def check_admin():
    if current_user.role != 2:
        return redirect(url_for('ecommerce.home'))

@admin.route('/')
@login_required
def index():
    """ Dashboard. """
    return render_template('views/index.html')

@admin.route('/products/', methods=['GET', 'POST'])
@login_required
def products():
    """ Load a list of products. """
    prods = Product.query.all()
    return render_template('views/products.html', action=None, products=prods)


@admin.route('/products/new-product', methods=['GET', 'POST'])
@login_required
def new_product():
    """ Create new product. """
    form = ProductForm()

    if form.validate_on_submit(): 
        product = Product()
        product.name = form.name.data
        product.information = form.information.data
        product.category = form.category.data
        product.stock = int(form.stock.data)
        product.price = int(form.price.data)
        product.visible = form.visible.data
        product.url = safe_url(product.name)['result']

        secure_filenames = []

        print(f'FORM: {form}')
        print(f'FORM FILES: {form.images}')
        print(f'FORM FILES DATA: {form.images.data}')

        for file in form.images.data:
            file_name = uuid4().hex
            file.save(path.join(current_app.config['UPLOAD_FOLDER'], file_name))
            secure_filenames.append(file_name)
        
        product.images = secure_filenames

        result = {'message': None, 'badge': None}
        
        try:
            result = {'message': 'Product saved.', 'badge': 'info'}
            db.session.add(product)
            db.session.commit()
        
        except Exception as e:
            result = {'message': f'Error: {e}', 'badge': 'error'}
            db.session.rollback()
        
        finally:
            flash(result['message'], result['badge'])

    return render_template('views/products.html', form=form, action='add')


@admin.route('/products/<product_url>/<action>', methods=['GET', 'POST'])
@login_required
def products_product(product_url, action):
    """ Edit, update and delete products. """
    pass


@admin.route('/categories/')
@login_required
def categories():
    pass


@admin.route('/orders/')
@login_required
def orders():
    pass


@admin.route('/files/')
@login_required
def files():
    pass


@admin.route('users')
@login_required
def users():
    pass

