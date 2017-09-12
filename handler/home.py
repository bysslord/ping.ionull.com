#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import Handler, render_template, BaseResponse


class Home(Handler):
    """
    home page
    """

    name = '主页'
    order = 1

    @staticmethod
    def render(**kwargs):
        """
        render home page
        :return:
        """
        return render_template('index.html', active=Home.url(), **kwargs)

    @staticmethod
    def alert(response: BaseResponse):
        """
        alert a message
        :param response:
        :return:
        """
        response.alert('test')
