from flask import current_app, Blueprint, render_template, request, redirect,\
                  url_for, flash
from flask_login import login_required, current_user
from admin.forms import ProductForm
from ecommerce.models import Product
from tools.database import db
from tools.tools import safe_url
from os import path
from uuid import uuid4


admin = Blueprint('admin',__name__, template_folder='templates',
        static_folder='static')

@admin.before_request
def check_admin():
    if not current_user.is_authenticated or current_user.role != 2:
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


@admin.route('/products/new-product/', methods=['GET', 'POST'])
@login_required
def new_product():
    """ Create new product. """
    form = ProductForm()

    if form.validate_on_submit():
        try:
            product = Product()
            product.name = form.name.data
            product.information = form.information.data
            product.category = form.category.data
            product.stock = int(form.stock.data)
            product.price = int(form.price.data)
            product.visible = form.visible.data
            product.url = safe_url(product.name)['result']

            secure_filenames = []

            name_in_use = Product.query.filter_by(name=product.name).first()
            
            if name_in_use:
                raise Exception('Product name already in use.')

            for file in form.images.data:
                if file.filename == '':
                    raise Exception('No selected file.')
                else:
                    file_name = uuid4().hex
                    directory = current_app.config['UPLOAD_FOLDER']
                    file.save(path.join(directory, file_name))
                    secure_filenames.append(file_name)
        
            if secure_filenames != []:
                product.images = secure_filenames

            result = {'message': 'Product saved.', 'badge': 'info'}
            
            db.session.add(product)
            db.session.commit()
        
        except Exception as e:
            result = {'message': f'{e}', 'badge': 'error'}
            db.session.rollback()
        
        finally:
            flash(result['message'], result['badge'])

    return render_template('views/products.html', form=form, action='add')


@admin.route('/products/<product_url>/<action>/', methods=['GET', 'POST'])
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


@admin.route('/users/')
@login_required
def users():
    pass

