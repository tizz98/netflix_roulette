import json
import urllib2
from urllib import urlencode

from constants import MEDIA_MAP, MOVIE_NETFLIX_REPR, \
    TV_SHOW_NETFLIX_REPR


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
            'title': unicode(self.title).encode('utf-8'),
        }

        if self.year is not None:
            params['year'] = self.year

        return urlencode(params)

    def _get_movie_data(self):
        url = '{0}?{1}'.format(self._api_url, self._get_url_parameters())

        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError:
            return None

        try:
            return json.load(response)
        except ValueError:
            return None

    def _set_attrs_none(self):
        for attr in self.__attrs__:
            setattr(self, attr, None)

    def _set_movie_data(self):
        data = self._get_movie_data()

        if data is None:
            self._set_attrs_none()
            self.is_on_netflix = False
        else:
            for attr, value in data.iteritems():
                setattr(self, attr, value)

            self.is_on_netflix = True
            self._data_set = True

    def get_readable_mediatype(self):
        if self._data_set:
            return MEDIA_MAP[self.mediatype]
        return ''

    def is_movie(self):
        return self.mediatype == MOVIE_NETFLIX_REPR

    def is_tv_show(self):
        return self.mediatype == TV_SHOW_NETFLIX_REPR
