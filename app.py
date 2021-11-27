from settings import app
from admin.urls import admin
from ecommerce.urls import ecommerce


# REGISTER CONTROLLERS
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(ecommerce, url_prefix='/')


if __name__ == '__main__':
    """ Run "app.py" for turn on the project. """
    app.run(debug=True)

