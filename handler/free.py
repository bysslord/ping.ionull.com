#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import Handler, BaseResponse
from util.session import is_logged_in


class Free(Handler):
    """
    home page
    """

    name = '免费试用'

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
