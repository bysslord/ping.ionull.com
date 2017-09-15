#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import Handler, BaseResponse
from util.session import is_logged_in


class Alert(Handler):
    """
    home page
    """

    @property
    def name(self):
        return '报警'

    @property
    def visible(self):
        return is_logged_in()

    @staticmethod
    def emit(response: BaseResponse, domain, username, ds_name, ds_id, when, tables: list):
        print('test')
        return 'success'

    @staticmethod
    def list(response: BaseResponse):
        """
        alert a message
        :param response:
        :return:
        """
        response.call('alert', ('test', 'success'))
