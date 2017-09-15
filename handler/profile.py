#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import Handler, BaseResponse, session
from util.session import is_logged_in


class Profile(Handler):
    """
    home page
    """

    @property
    def name(self):
        return session.get('username')

    @property
    def visible(self):
        return is_logged_in()

    @staticmethod
    def logout(response: BaseResponse):
        """
        alert a message
        :param response:
        :return:
        """
        response.redirect('/login')
