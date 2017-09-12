#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import Handler, render_template, BaseResponse


class About(Handler):
    """
    home page
    """

    name = '关于'
    order = 999

    @staticmethod
    def render(**kwargs):
        """
        render home page
        :return:
        """
        return render_template('about.html', active=About.url(), **kwargs)

    @staticmethod
    def alert(response: BaseResponse):
        """
        alert a message
        :param response:
        :return:
        """
        response.alert('test')
