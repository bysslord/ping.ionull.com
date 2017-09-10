#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import OrderedDict

from flask import Flask, g, render_template, redirect, request
from flask_sijax import Sijax, route
from sijax.response.base import BaseResponse
from util.db import db_session

__all__ = ['app', 'render_template', 'redirect', 'BaseResponse', 'request']

app = Flask(
    __name__, template_folder='../template', static_folder='../static'
)

Sijax(app)


@app.teardown_appcontext
def remove_session(exception=None):
    """
    clean up database session
    :return:
    """
    db_session.remove()


class AutoRoute(type):
    """
    Auto routing
    """

    route = OrderedDict()

    def __init__(cls, what, bases=None, extra=None):
        """
        :type cls: Handler
        :param what:
        :param bases:
        :param extra:
        """
        if object not in bases:
            print(f'Routing {cls.url()} -> {cls}')
            AutoRoute.route[cls.url()] = cls
        super().__init__(what, bases, extra)


class Handler(object, metaclass=AutoRoute):
    """
    Base Handler
    """

    @staticmethod
    def render(**kwargs):
        """
        render template
        :return:
        """
        raise NotImplementedError()

    @classmethod
    def url(cls):
        """
        route name
        :return:
        """
        return f'/{cls.__name__.lower()}'


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

    return handler.render(navbar=AutoRoute.route)
