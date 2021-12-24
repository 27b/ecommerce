from tools.database import db
from tools.views import ViewMixin
from flask import render_template, request, flash
from ecommerce.models import Category
from .forms import CategoryForm


# TESTING IF CLASS-BASED VIEWS ARE FEASIBLE
# /categories/               -> get / insert
# /categories/<id>/          -> get / update
# /categories/<id>/delete    -> delete

class Categories(ViewMixin):
    """ Class based view of categories. """

    def get(self):
        """ Views: list of categories and new product. """  
        view = request.args.get('view')
        self.context['view'] = view
        
        if view == None:
            self.context['categories'] = Category.query.all()
        else:
            form = CategoryForm()
            self.context['form'] = form

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
            else:
                raise Exception('Name already in use.')


class CategoriesEditor(ViewMixin):
    """ Class based view for individual and use actions. """

    def get(self, category_id):
        """ Get product. """
        category = Category.query.filter_by(id=category_id).first()
        self.context['category'] = category_id

    def post(self):
        """ Update and delete product. """
        pass

