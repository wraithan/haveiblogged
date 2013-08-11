#!/usr/bin/env python
import json
import logging
import os
from datetime import date

from flask import Flask

from lib.wp import MyWP


app = Flask(__name__)
app.debug = True
site_id = os.getenv('SITE_ID') or 55976772


@app.before_first_request
def setup_logging():
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)


@app.route('/')
def index():
    with open('templates/index.html') as f:
        return f.read()


@app.route('/status.json')
def status():
    wp = MyWP(site_id)
    categories = ('Gaming', 'Life', 'Programming')
    posted_in = set()
    today = date.today()
    start = today.replace(day=today.day-today.isoweekday())

    res = wp.get('sites/{site_id}/posts',
                 params={'after': start.isoformat()}).json()
    for post in res['posts']:
        posted_in.update(post['categories'].keys())

    return json.dumps(dict([(cat, cat in posted_in) for cat in categories]))


if __name__ == '__main__':
    app.run()
