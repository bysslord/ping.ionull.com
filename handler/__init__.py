#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, g, render_template, redirect, request
from flask_sijax import Sijax, route
from sijax.response.base import BaseResponse
from util.db import db_session
from handler.base import AutoRoute, Handler

from handler.home import Home
from handler.about import About
from handler.free import Free
from handler.login import Login
from handler.signup import SignUp

nav = {
    'left': [Home, About],
    'right': [Free, Login, SignUp]
}

__all__ = ['app', 'render_template', 'redirect', 'BaseResponse', 'request', 'Handler']

app = Flask(
    __name__, template_folder='../resource/template', static_folder='../resource/static'
)

Sijax(app)


@app.teardown_appcontext
def remove_session(exception=None):
    """
    clean up database session
    :return:
    """
    db_session.remove()


@route(app, '/<page>')
@route(app, '/')
def index(page: str = None):
    """
    index route
    :param page:
    :return:
    """
    if not page:
        page = 'home'
    handler: Handler = AutoRoute.route.get(f'/{page}')
    if not handler:
        return f'Page "{page}" not found', 404
    if g.sijax.is_sijax_request:
        # Sijax request detected - let Sijax handle it
        g.sijax.register_object(handler)
        return g.sijax.process_request()

    return handler.render(navbar=nav)
