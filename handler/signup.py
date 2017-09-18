#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import Handler, render_template, BaseResponse
from util.session import is_logged_in


class SignUp(Handler):
    """
    home page
    """

    name = '注册'

    @property
    def visible(self):
        return not is_logged_in()

    @staticmethod
    def alert(response: BaseResponse):
        """
        alert a message
        :param response:
        :return:
        """
        response.alert('test')
