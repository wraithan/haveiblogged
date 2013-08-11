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
