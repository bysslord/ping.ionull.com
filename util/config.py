#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'
import os
from configparser import RawConfigParser


config = RawConfigParser()
config.read(os.path.join(os.getcwd(), 'conf', 'offline.ini'))
