import json
import urllib2
from urllib import urlencode


__author__ = 'Elijah <elijah@elijahwilson.me>'
__version__ = '0.13'


class NetflixMedia(object):
    __attrs__ = [
        'rating', 'poster', 'mediatype', 'release_year', 'show_cast',
        'category', 'summary', 'director', 'show_id', 'is_on_netflix'
    ]

    _api_url = 'http://netflixroulette.net/api/api.php'
    _data_set = False

    def __init__(self, title, year=None):
        self.title = title
        self.year = year

        self._set_movie_data()

    def __repr__(self):
        return "<NetflixMedia(title='{0}', year='{1}')>".format(
            self.title, self.year)

    def _get_url_parameters(self):
        params = {
            'title': self.title,
        }

        if self.year is not None:
            params['year'] = self.year

        return urlencode(params)

    def _get_movie_data(self):
        url = '{0}?{1}'.format(self._api_url, self._get_url_parameters())
        response = urllib2.urlopen(url)
        try:
            return json.load(response)
        except ValueError:
            return None

    def _set_attrs_none(self):
        for attr in self.__attrs__:
            setattr(self, attr, None)

    def _set_movie_data(self):
        data = self._get_movie_data()

        if 'errorcode' in data:
            self._set_attrs_none()
            self.is_on_netflix = False

        for attr, value in data.iteritems():
            setattr(self, attr, value)

        self.is_on_netflix = True
        self._data_set = True

    def get_readable_mediatype(self):
        if self._data_set:
            return 'TV Show' if self.mediatype == 1 else 'Movie'
        return ''
