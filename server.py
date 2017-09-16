#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from handler import app
from util.config import config
from util.models import db

CWD = os.getcwd()

app.config['SIJAX_STATIC_PATH'] = os.path.join(CWD, 'resource', 'static', 'js', 'sijax')
app.config['SIJAX_JSON_URI'] = os.path.join(CWD, 'resource', 'static', 'js', 'sijax', 'json2.js')
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('db', 'uri')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


if __name__ == '__main__':
    db.init_app(app)
    app.run(host='0.0.0.0', port=config.getint('global', 'port'), debug=True if config.getint('global', 'debug') else False)
