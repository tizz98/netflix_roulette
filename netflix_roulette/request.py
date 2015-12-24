import six
import json
from six.moves import urllib

from . import exceptions


class Request(urllib.request.Request):
    _base_url = "http://netflixroulette.net/api/api.php"

    def __init__(self, **kwargs):
        self._kwargs = kwargs
        kwargs = {}

        for k, v in self._kwargs.items():
            # Make sure we only encode strings but NOT unicode
            if not isinstance(v, six.text_type) \
               and isinstance(v, six.string_types):
                v = six.u(v).encode('utf-8')

            kwargs[k] = v

        url = '{0}?{1}'.format(self._base_url, urllib.parse.urlencode(kwargs))

        urllib.request.Request.__init__(self, url)
        self.add_header('Accept', 'application/json')
        self.lifetime = 3600  # 1 hour

    def open(self):
        try:
            return urllib.request.urlopen(self)
        except urllib.error.HTTPError as e:
            raise exceptions.NetflixRouletteHTTPError(e)

    def json(self):
        try:
            fp = self.open()
            data = json.loads(fp.read().decode('utf-8'))
        except exceptions.NetflixRouletteHTTPError as e:
            try:
                data = json.loads(e.response.decode('utf-8'))
            except Exception as e:
                raise exceptions.NetflixRouletteError(e)

        return data
