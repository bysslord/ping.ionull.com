#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

app = Flask(__name__)
socketio = SocketIO(app)

scheduler = BackgroundScheduler(
    jobstores={'default': SQLAlchemyJobStore(os.environ['SQL_ALCHEMY_URI'])}
)


def ping(url):
    print(url)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/job/ping', methods=['DELETE', 'POST'])
def job_ping():
    scheduler.add_job(ping, IntervalTrigger(seconds=1), args=(request.form['url'],))
    return 'success'


if __name__ == '__main__':
    scheduler.start()
    socketio.run(app, debug=True)
