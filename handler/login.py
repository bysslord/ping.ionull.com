#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import Handler, render_template, BaseResponse


class Login(Handler):
    """
    home page
    """

    name = '登录'

    @staticmethod
    def render(**kwargs):
        """
        render home page
        :return:
        """
        return render_template('login.html', active=Login.url(), **kwargs)

    @staticmethod
    def alert(response: BaseResponse):
        """
        alert a message
        :param response:
        :return:
        """
        response.alert('test')
