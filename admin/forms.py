from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length

# PRODUCT
class CategoryForm():
    """ Used in /admin-panel for add and edit categories. """
    name = StringField('Category Name', validators = [
        DataRequired(), Length(min=4, max=20)
    ])
    visible = BooleanField()
    submit = SubmitField()


class ProductForm(FlaskForm):
    """ Used in /admin-panel for add and edit products. """ 
    name = StringField('Product Name', validators = [
        DataRequired(), Length(min=5, max=200)
    ])
    information = StringField('Product Information', validators = [
        DataRequired(), Length(min=20, max=256)
    ])
    category = StringField('Product Category', validators = [
        DataRequired(), Length(min=10, max=20)
    ])
    stock = IntegerField('Product Stock', validators = [
        DataRequired(), Length(min=1, max=5)
    ])
    price = IntegerField('Product Price', validators = [
        DataRequired(), Length(min=1, max=10)
    ])
    visible = BooleanField()
    submit = SubmitField()
