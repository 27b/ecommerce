from flask import render_template, redirect, url_for, request, flash
from tools.database import db
from tools.views import ViewMixin
from ecommerce.models import Category, Product
from .forms import CategoryForm


class Categories(ViewMixin):
    """ Class based view of categories. """

    def get(self):
        """ Views: list of categories and new product. """
        view = request.args.get('view')
        self.context['view'] = view

        if view == 'add':
            self.context['form'] = CategoryForm()
        else:
            self.context['categories'] = Category.query.all()        

    def post(self):
        """ Create new product. """
        form = CategoryForm()

        if form.validate_on_submit():
            name = form.name.data
            visible = form.visible.data
            new_category = Category(name=name, visible=visible)

            if not Category.query.filter_by(name=name).first():
                db.session.add(new_category)
                db.session.commit()
                flash('Category Updated!', 'info')
            else:
                raise Exception('Name already in use.')
        else:
            flash('Invalid form', 'error')


class CategoriesEditor(ViewMixin):
    """ Class based view for individual and use actions. """

    def get(self, category_id: int):
        """ Get product and set data on a form. """
        category = Category.query.filter_by(id=category_id).first()

        if category:
            linked_products = Product.query.filter_by(category=category_id)
            form = CategoryForm(name=category.name, visible=category.visible)
            self.context['view'] = 'category'
            self.context['category_id'] = category_id
            self.context['form'] = form
            self.context['products'] = linked_products
        else:
            raise Exception('Wrong category id.')

    def post(self, category_id):
        """ Update and delete product. """
        form = CategoryForm()
        category = Category.query.filter_by(id=category_id).first()
        name_in_db = Category.query.filter_by(name=form.name.data).first()
        
        if category and form.validate_on_submit():
            if not name_in_db or category.name == form.name.data:
                category.name = form.name.data
                category.visible = form.visible.data
                db.session.commit()
                flash('Product updated!', 'info')
            else:
                raise Exception('Name already in use.')
        else:
            raise Exception('Wrong category id.')        
