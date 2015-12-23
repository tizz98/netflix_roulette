import json
import urllib2
from urllib import urlencode

from .exceptions import NetflixRouletteHTTPError


class Request(urllib2.Request):
    _base_url = "http://netflixroulette.net/api/api.php"

    def __init__(self, **kwargs):
        self._kwargs = kwargs
        kwargs = {}

        for k, v in self._kwargs.items():
            kwargs[k] = unicode(v).encode('utf-8')

        url = '{0}?{1}'.format(self._base_url, urlencode(kwargs))

        urllib2.Request.__init__(self, url)
        self.add_header('Accept', 'application/json')
        self.lifetime = 3600  # 1 hour

    def add_data(self, data):
        urllib2.Request.add_data(self, urlencode(data))

    def open(self):
        try:
            return urllib2.urlopen(self)
        except urllib2.HTTPError, e:
            raise NetflixRouletteHTTPError(e)

    def json(self):
        try:
            data = json.load(self.open())
        except NetflixRouletteHTTPError, e:
            try:
                data = json.loads(e.response)
            except:
                raise e

        return data
