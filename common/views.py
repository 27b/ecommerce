from flask import request, redirect, url_for, abort, render_template, flash
from flask.views import View


class MethodView(View):
    """
    This class extends other class with a state and functions based on Flask
    View, you can re-write .get(), .post(), .put() and .delete() methods.
    """
    methods = ['GET', 'POST']

    def __init__(self, template_name: str = None, url_to_redirect: str = None):
        self.template_name = template_name
        self.url_to_redirect = url_to_redirect
        self.context = {'redirect': False, 'reload': False}

    def render_template(self, context):
        """ Returns a template with template_name and context. """
        return render_template(self.template_name, **context)

    def move_to(self, direction: str) -> None:
        """ Used in views how redirect(url_for(...)). """
        self.context['redirect'] = direction

    def reload_page(self) -> None:
        """
        Change reload context to True, in dispath_request if
        reload context it's True use redirect and url_for to go
        to the base endpoint of the request.
        """
        self.context['reload'] = True

    def dispatch_request(self, **kwargs):
        """
        Depending on the method of the query, it executes a method
        of the class, if the method is post refresh the page.
        """
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
                abort(404)

        except Exception as error:
            flash(error, 'error')

        # If use .move_to()
        if self.context['redirect']:
            return redirect(url_for(self.context['redirect'], **kwargs))
        
        elif request.method == 'GET':
            return self.render_template(self.context)
        
        elif request.method == 'POST' or self.context['reload']:
            # If only exist post method (not .get method = not render template)
            try:
                if self.template_name:
                    return redirect(url_for(request.endpoint, **kwargs))
                elif not self.template_name and self.url_to_redirect:
                    return redirect(url_for(self.url_to_redirect, **kwargs))
                return {'status': 200, 'error': 'Not view'}
            except Exception as error:
                return error
        else:
            return self.render_template(self.context)

    def get(self, **kwargs):
        """
        Pass to this method the code that you want to be executed
        when the request method is get.
        """
        raise NotImplementedError

    def post(self, **kwargs):
        """
        Pass to this method the code that you want to be executed
        when the request method is post.
        """
        raise NotImplementedError
    
    def put(self, **kwargs):
        """
        Pass to this method the code that you want to be executed
        when the request method is put.
        """
        raise NotImplementedError

    def delete(self, **kwargs):
        """
        Pass to this method the code that you want to be executed
        when the request method is delete.
        """
        raise NotImplementedError
