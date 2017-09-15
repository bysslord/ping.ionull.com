#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from flask import session


def is_logged_in():
    return 'username' in session
