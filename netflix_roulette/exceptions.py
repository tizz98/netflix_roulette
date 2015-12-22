class NetflixRouletteError(Exception):
    pass


class NetflixRouletteHTTPError(NetflixRouletteError):
    def __init__(self, error):
        self.http_error_number = error.code
        self.response = error.fp.read()
        super(NetflixRouletteHTTPError, self).__init__(str(error))
