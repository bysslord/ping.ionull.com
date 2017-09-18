#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import Handler, render_template, BaseResponse
from util.session import is_logged_in


class Index(Handler):
    """
    home page
    """

    name = '主页'

    @property
    def visible(self):
        return True

    @staticmethod
    def alert(response: BaseResponse):
        """
        alert a message
        :param response:
        :return:
        """
        response.alert('test')
