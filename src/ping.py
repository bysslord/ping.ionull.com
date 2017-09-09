#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import glob
from handler import app

CWD = os.path.dirname(__file__)
os.chdir(CWD)

app.config['SIJAX_STATIC_PATH'] = os.path.join(CWD, 'static', 'js', 'sijax')
app.config['SIJAX_JSON_URI'] = os.path.join(CWD, 'static', 'js', 'sijax', 'json2.js')


def _auto_import():
    for file in glob.glob('handler/*.py'):
        mod = os.path.basename(file).split('.')[0]
        if mod != '__init__':
            __import__(f'handler.{mod}')


if __name__ == '__main__':
    _auto_import()
    app.run(port=5000, debug=True)
