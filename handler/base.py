#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'


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
    order = 999

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

