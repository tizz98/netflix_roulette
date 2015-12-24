from .util import Element
from .request import Request
from .constants import MEDIA_MAP, MOVIE_NETFLIX_REPR, \
    TV_SHOW_NETFLIX_REPR


class NetflixMedia(Element):
    __attrs__ = [
        'rating', 'poster', 'mediatype', 'release_year', 'show_cast',
        'category', 'summary', 'director', 'show_id', 'is_on_netflix'
    ]

    repr_data_items = [
        'title',
        'year',
    ]

    def __init__(self, title, year=None, **kwargs):
        self.title = title
        self.year = year
        self.kwargs = kwargs

        if not self.kwargs:
            super(NetflixMedia, self).__init__()
        else:
            self._set_data(kwargs)

    def _set_data(self, data_dict):
        for attr, value in data_dict.items():
            setattr(self, attr, value)

    def _populate(self):
        params = {
            'title': self.title,
        }

        if self.year:
            params['year'] = self.year

        response = Request(**params)
        data = response.json()

        if 'errorcode' in data:
            self._set_attrs_none()
            self.is_on_netflix = False
        else:
            self._set_data(data)
            self.is_on_netflix = True

        super(NetflixMedia, self)._populate()

    def get_readable_mediatype(self):
        if self._data_set:
            return MEDIA_MAP[self.mediatype]
        return ''

    def is_movie(self):
        return self.mediatype == MOVIE_NETFLIX_REPR

    def is_tv_show(self):
        return self.mediatype == TV_SHOW_NETFLIX_REPR


class PersonWithMedia(Element):
    __attrs__ = ['media', 'is_on_netflix']

    repr_data_items = [
        'name',
    ]

    url_query_param = ''
    media_cls = NetflixMedia

    def __init__(self, name):
        self.name = name

        super(PersonWithMedia, self).__init__()

    def _populate(self):
        response = Request(**{self.url_query_param: self.name})
        data = response.json()

        if 'errorcode' in data:
            self.media = []
            self.is_on_netflix = False
        else:
            self.media = [
                self.media_cls(media) for media in data
            ]
            self.is_on_netflix = True

        super(PersonWithMedia, self)._populate()


class NetflixDirector(PersonWithMedia):
    url_query_param = 'director'


class NetflixActor(PersonWithMedia):
    url_query_param = 'actor'
