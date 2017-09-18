#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from handler import Handler, BaseResponse
from util.session import is_logged_in
from util.models.Alert import AlertModel


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

    @property
    def render_kwargs(self):
        return {
            'cards': AlertModel.query.all()
        }

    @staticmethod
    def list(response: BaseResponse, filter_by: dict, order_by: str):
        """
        alert a message
        :param order_by:
        :param filter_by:
        :param response:
        :return:
        """
        print(AlertModel.query)
