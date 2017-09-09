#!/usr/bin/python
# -*- coding: utf-8 -*-
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

    route = {}

    def __init__(cls, what, bases=None, extra=None):
        """
        :type cls: Handler
        :param what:
        :param bases:
        :param extra:
        """
        print(cls)
        if object not in bases:
            AutoRoute.route[cls.__name__.lower()] = cls
        super().__init__(what, bases, extra)


class Handler(object, metaclass=AutoRoute):
    """
    Base Handler
    """

    @staticmethod
    def render():
        """
        render template
        :return:
        """
        raise NotImplementedError()


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
    handler: Handler = AutoRoute.route.get(page)
    if not handler:
        return f'Page "{page}" not found', 404
    if g.sijax.is_sijax_request:
        # Sijax request detected - let Sijax handle it
        g.sijax.register_object(handler)
        return g.sijax.process_request()

    return handler.render()
