import json
import os
from datetime import date

import requests


class MyWP(object):

    def __init__(self, site_id):
        self.site_id = site_id
        self.url = 'https://public-api.wordpress.com/rest/v1/{endpoint}/'

    def build_url(self, endpoint):
        ep = endpoint.format(site_id=self.site_id)
        return self.url.format(endpoint=ep)

    def get(self, endpoint, **kwargs):
        return requests.get(self.build_url(endpoint), **kwargs)

    def post(self, endpoint, data, **kwargs):
        return requests.post(self.build_url(endpoint), data=data, **kwargs)


site_id = os.getenv('SITE_ID') or 55976772

if __name__ == '__main__':
    wp = MyWP(site_id)
    categories = ('Gaming', 'Life', 'Programming')
    posted_in = set()
    today = date.today()
    start = today.replace(day=today.day-today.isoweekday())

    res = wp.get('sites/{site_id}/posts',
                 params={'after': start.isoformat()}).json()
    for post in res['posts']:
        posted_in.update(post['categories'].keys())

    for cat in categories:
        print '{}: {}'.format(cat, cat in posted_in)
