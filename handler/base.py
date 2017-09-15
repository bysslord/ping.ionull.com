#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import render_template


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
        if object not in bases:
            print(f'Routing {cls.url()} -> {cls}')
            AutoRoute.route[cls.url()] = cls
        super().__init__(what, bases, extra)


class Handler(object, metaclass=AutoRoute):
    """
    Base Handler
    """
    def __init__(self):
        pass

    @property
    def visible(self):
        return True

    @classmethod
    def render(cls, navbar: dict):
        """
        render template
        :return:
        """
        return render_template(f'{cls.url()}.html', navbar=navbar)

    @classmethod
    def url(cls):
        """
        route name
        :return:
        """
        return cls.__name__.lower()

