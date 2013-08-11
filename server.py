#!/usr/bin/env python
import json
import logging

from flask import Flask

from lib.wp import MyWP


app = Flask(__name__)
app.debug = True


@app.before_first_request
def setup_logging():
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)


@app.route('/')
def index():
    with open('templates/index.html') as f:
        return f.read()


@app.route('/stats.json')
def stats():
    wp = MyWP
    return json.dumps((), sort_keys=False)


if __name__ == '__main__':
    app.run()
