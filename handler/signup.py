#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import Handler, render_template, BaseResponse


class SignUp(Handler):
    """
    home page
    """

    name = '注册'
    order = 1

    @staticmethod
    def alert(response: BaseResponse):
        """
        alert a message
        :param response:
        :return:
        """
        response.alert('test')
