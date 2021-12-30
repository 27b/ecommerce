from flask import render_template, redirect, url_for, request, flash
from tools.database import db
from tools.views import ViewMixin
from ecommerce.models import Category, Product, Order
from .forms import CategoryForm


class Categories(ViewMixin):
    """ Class based view of categories. """

    def get(self):
        """ Views: list of categories and new product. """
        view = request.args.get('view')
        visible = request.args.get('visible')

        self.context['view'] = view

        if view == 'add':
            self.context['category_form'] = CategoryForm()
        elif visible == "0" or visible == "1":
            self.context['categories'] = Category.query.filter_by(visible=visible)
        else:
            self.context['categories'] = Category.query.all()

    def post(self):
        """ Create new product. """
        category_form = CategoryForm()

        if category_form.validate_on_submit():
            name = category_form.name.data
            visible = category_form.visible.data
            
            new_category = Category(name=name, visible=visible)

            if not Category.query.filter_by(name=name).first():
                db.session.add(new_category)
                db.session.commit()
                flash('Category created!', 'info')
            else:
                raise Exception('Name already in use.')
        else:
            flash('Invalid form', 'error')


class CategoriesEditor(ViewMixin):
    """ Class based view for individual and use actions. """

    def get(self, category_id):
        """ Get product and set data on a form. """
        category = Category.query.filter_by(id=category_id).first()

        if category:
            linked_products = Product.query.filter_by(category=category.name)
            category_form = CategoryForm(name=category.name, visible=category.visible)
            self.context['view'] = 'category'
            self.context['category_id'] = category_id
            self.context['category_form'] = category_form
            self.context['products'] = linked_products
        else:
            raise Exception('Wrong category id.')

    def post(self, category_id):
        """ Update and delete category. """
        category = Category.query.filter_by(id=category_id).first()
        category_form = CategoryForm()

        if category and category_form.validate_on_submit():
            name_in_db = Category.query.filter_by(name=category_form.name.data).first()
            
            if not name_in_db or category.name == category_form.name.data:
                category.name = category_form.name.data
                category.visible = category_form.visible.data
                db.session.commit()
                flash('Category updated!', 'info')
            else:
                raise Exception('Name already in use.') 
        else:
            raise Exception('Wrong category id.')


class CategoriesEditorActions(ViewMixin):
    methods = ['POST']

    def post(self, category_id, action):
        category = Category.query.filter_by(id=category_id).first()
        if category:
            if action == 'delete':
                db.session.delete(category)
                db.session.commit()
                flash('Category deleted!', 'info')
            else:
                raise Exception('The action does not exist.')
        else:
            raise Exception('Icorrect name, try again.')


class Orders(ViewMixin):
    """ Class based view of orders. """
    
    def get(self):
        print('Hello World')

    def post(self):
        print('Hello World')
        

class OrdersEditor(ViewMixin):
    """ Class based view for individual and use actions. """
    
    def get(self, order_id):
        print('Hello World')

    def post(self, order_id):
        print('Hello World')
