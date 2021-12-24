from tools.views import ViewMixin
from flask import render_template, flash
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
        self.context['categories'] = [{'name': 'First category'}]

    def post(self):
        """ Create new product. """


class CategoriesEditor(ViewMixin):
    """ Class based view for individual and use actions. """

    def get(self, category_id):
        """ Get product. """
        category = Category.query.filter_by(id=category_id).first()
        self.context['category'] = category

    def post(self):
        """ Update and delete product. """
        pass

