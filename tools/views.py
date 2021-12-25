from flask import request, redirect, url_for, abort, render_template, flash
from flask.views import View


class ViewMixin(View):
    """
    This class extends other class with a state and functions based on Flask
    View, you can re-write .get() and .post() methods.
    """
    methods = ['GET', 'POST']

    def __init__(self, template_name: str):
        self.template_name = template_name
        self.context = {}
    
    def reload_page(self) -> None:
        self.context['reload'] = True

    def render_template(self, context):
        """ Returns a temaplate with template_name and context"""
        return render_template(self.template_name, **context)

    def dispatch_request(self, **kwargs):
        try:
            if request.method == 'GET':
                self.get(**kwargs)
            elif request.method == 'POST':
                self.post(**kwargs)
            else:
                abort(500)

        except Exception as error:
            flash(error, 'error')
            
        finally:
            pass

        return self.render_template(self.context)

    def get(self, **kwargs):
        """ Method not implemented. """
        pass

    def post(self, **kwargs):
        """ Method not implemented. """
        pass


class ViewExtendedMixin(ViewMixin, View):
    """
    This class extends other class with a state and functions based on Flask
    View, you can re-write .get(), post(), .put() and .delete() methods.
    """
    methods = ['GET', 'POST', 'PUT', 'DELETE']

    def dispatch_request(self, **kwargs):
        try:
            if request.method == 'GET':
                self.get(**kwargs)
            elif request.method == 'POST':
                self.post(**kwargs)
            elif request.method == 'PUT':
                self.put(**kwargs)
            elif request.method == 'DELETE':
                self.delete(**kwargs)
            else:
                abort(500)

        except Exception as error:
            print(error)

        finally:
            return self.end_method()

    def put(self, **kwargs):
        """ Method not implemented. """
        pass

    def delete(self, **kwargs):
        """ Method not implemented. """
        pass

