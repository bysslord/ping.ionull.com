#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'
from . import db


class AlertModel(db.Model):
    __tablename__ = 't_alert'

    id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    domain = db.Column('domain', db.String, nullable=False)

    def __init__(self):
        pass
