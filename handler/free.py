#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import Handler, render_template, BaseResponse


class Free(Handler):
    """
    home page
    """

    name = '免费试用'

    @staticmethod
    def alert(response: BaseResponse):
        """
        alert a message
        :param response:
        :return:
        """
        response.alert('test')
