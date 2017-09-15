#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import Handler, render_template, BaseResponse


class About(Handler):
    """
    home page
    """

    @property
    def name(self):
        return '关于'

    @staticmethod
    def alert(response: BaseResponse):
        """
        alert a message
        :param response:
        :return:
        """
        response.alert('test')
