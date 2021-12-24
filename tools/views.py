from flask import request, abort, render_template, flash
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

    def render_template(self, context):
        """ Returns a temaplate with template_name and context"""
        return render_template(self.template_name, **context)

    def dispatch_request(self):
        try:
            if request.method == 'GET': self.get() 
            elif request.method == 'POST': self.post()
            else: abort(500)

        except Exception as error:
            flash(error, 'error')
            
        finally:
            return self.render_template(self.context)

    def get(self):
        """ Method not implemented. """
        pass

    def post(self):
        """ Method not implemented. """
        pass


class ViewExtendedMixin(ViewMixin, View):
    """
    This class extends other class with a state and functions based on Flask
    View, you can re-write .get(), post(), .put() and .delete() methods.
    """

    def dispatch_request(self):
        try:
            if request.method == 'GET': self.get()
            elif request.method == 'POST': self.post()
            elif request.method == 'PUT': self.put()
            elif request.method == 'DELETE': self.delete()
            else: abort(500)

        except Exception as error:
            print(error)

        finally:
            return self.end_method()

    def put(self):
        """ Method not implemented. """
        pass

    def delete(self):
        """ Method not implemented. """
        pass

