from tools.views import CRUDMixin
from flask import render_template

from ecommerce.models import Category


class CategoriesView(CRUDMixin):
    """ Class based view of Orders. """

    def __init__(self, template_name: str = None):
        self.template_name = template_name
        #self.form = form

    def get(self):
        print('Hello World')

    def post(self):
        pass


class CRUDCategories(CRUDMixin):
    """ Class based view of Categories. """

    def get(self):
        pass

    def post(self):
        pass

