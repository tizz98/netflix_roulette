class Element(object):
    __attrs__ = []
    repr_data_items = []

    def __init__(self):
        self._populate()

    def __repr__(self):
        return u'<{0.__class__.__name__} {1}>'.format(
            self, u' '.join([u"{0}='{1}'".format(k, getattr(self, k, None))
                             for k in self.repr_data_items]),
        ).encode('utf-8')

    def _populate(self):
        self._data_set = True

    def _set_attrs_none(self):
        for attr in self.__attrs__:
            setattr(self, attr, None)
