from flask import current_app, Blueprint, render_template, request, redirect,\
                  url_for, flash
from flask_login import login_required, current_user
from admin.forms import ProductForm
from admin.models import Notification
from ecommerce.models import Product
from tools.database import db
from tools.tools import safe_url, create_notification
from os import path
from uuid import uuid4


admin = Blueprint('admin', __name__, template_folder='templates',
        static_folder='static')

@admin.before_request
def check_admin():
    if not current_user.is_authenticated or current_user.role != 2:
        return redirect(url_for('ecommerce.home'))


@admin.context_processor
def inject_notifications():
    notifications = Notification.query \
                                .order_by(Notification.datetime.desc()) \
                                .limit(20) \
                                .all() \
    
    return dict(notifications=notifications)


@admin.route('/')
@login_required
def index():
    """ Dashboard. """
    return render_template('views/index.html')


@admin.route('/products/', methods=['GET', 'POST'])
@login_required
def products():
    """ Load a list of products. """
    visible = request.args.get('visible')

    if visible: prods = Product.query.filter_by(visible=visible)
    else: prods = Product.query.all()
    
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

            name_in_use = Product.query.filter_by(name=product.name).first()
            url_in_use = Product.query.filter_by(url=product.url).first()

            if name_in_use: raise Exception('Name already in use.')
            if url_in_use: raise Exception('URL in use, change the name.')

            secure_filenames = []

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

            status = {'message': 'Product saved.', 'badge': 'info'}
            
            db.session.add(product)
            db.session.commit()

        except Exception as e:
            status = {'message': f'{e}', 'badge': 'error'}
            db.session.rollback()
        
        finally:
            flash(status['message'], status['badge'])
            if status['badge'] == 'info':
                title = 'New product'
                text = f'The product {product.name} has been created.'
                create_notification(title, text)

    return render_template('views/products.html', form=form, action='add')


@admin.route('/products/<product_url>/<action>/', methods=['GET', 'POST'])
@login_required
def products_action(product_url, action):
    """ Edit, update and delete products. """
    product = Product.query.filter_by(url=product_url).first()

    form = ProductForm()

    # GET PRODUCT
    if product and request.method == 'GET' and action == 'update':
        form.name.data = product.name
        form.information.data = product.information
        form.category.data = product.category
        form.stock.data = product.stock
        form.price.data = product.price
        form.visible.data = product.visible

        return render_template('views/products.html', form=form,\
                                action='update', product=product)

    # UPDATE PRODUCT
    if request.method == 'POST' and action == 'update':
        if form.validate_on_submit():
            try:
                status = {'message': 'Product updated!', 'badge': 'info'}
                
                secure_name = form.name.data
                secure_url = safe_url(secure_name)['result']

                name_used = Product.query.filter_by(name=secure_name).first()
                url_used = Product.query.filter_by(url=secure_url).first()

                if name_used and name_used.id != product.id:
                    raise Exception(f'Name already in use.')

                if url_used and url_used.id != product.id:
                    raise Exception('URL in use, change the name.')

                product.name = secure_name
                product.information = form.information.data
                product.category = form.category.data
                product.stock = form.stock.data
                product.price = form.price.data
                product.visible = form.visible.data
                product.url = secure_url

                # db.session.merge(product)
                db.session.commit()

            except Exception as error:
                status = {'message': f'{error}', 'badge': 'error'}
                db.session.rollback()
            
            finally:
                flash(status['message'], status['badge'])
                if status['badge'] == 'info':
                    title = 'Product updated'
                    text = f'The product {product.name} has been updated.'
                    create_notification(title, text)

                return redirect(url_for('admin.products'))

    # DELETE PRODUCT
    if request.method == 'POST' and action == 'delete':
        try:
            status = {'message': 'Product deleted', 'badge': 'info'}
            product.deleted = True
            db.session.commit()

        except Exception as error:
            status = {'message': f'{error}', 'badge': 'error'}
            db.session.rollback()
            return redirect(url_for('admin'))
        
        finally:
            flash(status['message'], status['badge'])
            if status['badge'] == 'info':
                title = 'Product deleted'
                text = f'The product {product.name} has been deleted.'
                create_notification(title, text)

        return redirect(url_for('admin.products'))


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

