from flask import request, abort, render_template
from flask.views import View


class CRUDMixin(View):
    """ Implement basic CRUD methods. """
    methods = ['GET', 'POST']

    def __init__(self, template_name: str):
        self.template_name = template_name

    def render_template(self, context):
        return render_template(self.template_name, **context)

    def dispatch_request(self):
        try:
            if request.method == 'GET': self.get()
            elif request.method == 'POST': self.post()
            else: abort(500)

        except Exception as error:
            print(error)

        finally:
            pass

        return render_template(self.template_name)

    def get(self):
        """ Method not implemented. """
        pass

    def post(self):
        """ Method not implemented. """
        pass


class CRUDExtendedMixin(CRUDMixin, View):
    """ Implement extended CRUD methods. """
    methods = ['GET', 'POST', 'PUT', 'DELETE']

    def dispatch_request(self):
        try:
            if request.method == 'GET': self.get()
            elif request.method == 'POST': self.post()
            elif request.method == 'PUT': self.put()
            elif request.method == 'DELETE': self.delete()
            else: abort(500)

        except Exception as error:
            print(error)

    def put(self):
        """ Method not implemented. """
        pass

    def delete(self):
        """ Method not implemented. """
        pass

