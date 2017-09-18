#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import Handler, render_template, BaseResponse, redirect
from util.session import session, is_logged_in


class Login(Handler):
    """
    home page
    """

    name = '登录'

    @property
    def visible(self):
        return not is_logged_in()

    @staticmethod
    def login(response: BaseResponse, username: str, password: str):
        """
        alert a message
        :param password:
        :param username:
        :param response:
        :return:
        """
        if username and password:
            session['username'] = username
            response.redirect('/')
        else:
            response.alert('error')

    def render(self, navbar: dict):
        if is_logged_in():
            return redirect('/profile')
        return super(Login, self).render(navbar=navbar)
