#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from handler import app

CWD = os.getcwd()

app.config['SIJAX_STATIC_PATH'] = os.path.join(CWD, 'resource', 'static', 'js', 'sijax')
app.config['SIJAX_JSON_URI'] = os.path.join(CWD, 'resource', 'static', 'js', 'sijax', 'json2.js')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
