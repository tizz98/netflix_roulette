import six
import json

if six.PY2:
    from urllib2 import Request as UrllibRequest
    from urllib2 import urlopen
    from urllib2 import HTTPError
    from urllib import urlencode
elif six.PY3:
    from urllib.request import Request as UrllibRequest
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from urllib.parse import urlencode
    unicode = str

from .exceptions import NetflixRouletteHTTPError


class Request(UrllibRequest):
    _base_url = "http://netflixroulette.net/api/api.php"

    def __init__(self, **kwargs):
        self._kwargs = kwargs
        kwargs = {}

        for k, v in self._kwargs.items():
            kwargs[k] = unicode(v).encode('utf-8')

        url = '{0}?{1}'.format(self._base_url, urlencode(kwargs))

        UrllibRequest.__init__(self, url)
        self.add_header('Accept', 'application/json')
        self.lifetime = 3600  # 1 hour

    def open(self):
        try:
            return urlopen(self)
        except HTTPError as e:
            raise NetflixRouletteHTTPError(e)

    def json(self):
        try:
            data = json.loads(self.open().read().decode('utf-8'))
        except NetflixRouletteHTTPError as e:
            try:
                data = json.loads(e.response)
            except:
                raise e

        return data
