#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, g, render_template
from flask_sijax import Sijax, route, Response

app = Flask(
    __name__, template_folder='template', static_folder='static'
)

CWD = os.path.dirname(__file__)
os.chdir(CWD)

app.config['SIJAX_STATIC_PATH']=os.path.join(CWD, 'static', 'js', 'sijax')
app.config['SIJAX_JSON_URI']=os.path.join(CWD, 'static', 'js', 'sijax', 'json2.js')

Sijax(app)


_router = {}


class AutoRoute(type):
    def __init__(cls, what, bases=None, dict=None):
        """
        :type cls: Handler
        :param what:
        :param bases:
        :param dict:
        """
        print(cls._route(), bases)
        super().__init__(what, bases, dict)


class Handler(object, metaclass=AutoRoute):

    @classmethod
    def _route(cls):
        if cls.__name__ == 'Handler':
            return '/', 'index.html'
        return f'{str(cls.__name__).lower()}', f'{str(cls.__name__).lower()}.html'

    @staticmethod
    def render():
        return render_template(Handler.template())


class Test(Handler):

    @staticmethod
    def log(response: Response, *args, **kwargs):
        print(args, kwargs)


@app.route('/')
def index():
    return render_template('index.html')


@route(app, '/test')
def test():
    if g.sijax.is_sijax_request:
        # Sijax request detected - let Sijax handle it
        g.sijax.register_callback('say_hi', str)
        return g.sijax.process_request()

    return 'test'


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=5000, debug=True)
