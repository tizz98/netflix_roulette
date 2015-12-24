# coding=utf-8
import netflix_roulette
from netflix_roulette.constants import TV_SHOW_STR, MOVIE_STR


# Note: testing with specific media will prove to not be reliable
def on_netflix_movie_test():
    media = netflix_roulette.NetflixMedia('The Avengers')
    assert media.is_on_netflix is True


def not_on_netflix_movie_test():
    media = netflix_roulette.NetflixMedia('Home', year=2015)
    print(media.__dict__)
    assert media.is_on_netflix is False


def movietype_tv_show_test():
    media = netflix_roulette.NetflixMedia('The Boondocks')
    assert media.get_readable_mediatype() == TV_SHOW_STR


def movietype_movie_test():
    media = netflix_roulette.NetflixMedia('The Avengers')
    assert media.get_readable_mediatype() == MOVIE_STR


def movie_test_with_year_test():
    media = netflix_roulette.NetflixMedia('The Boondocks', year=2005)
    assert media.year == 2005


def unicode_title_test():
    # Make sure unicode is properly encoded
    media = netflix_roulette.NetflixMedia('H βουλευτινα')


def is_movie_func_test():
    assert callable(netflix_roulette.NetflixMedia.is_movie)


def is_tv_show_func_test():
    assert callable(netflix_roulette.NetflixMedia.is_tv_show)


def is_movie_media_test():
    media = netflix_roulette.NetflixMedia('The Avengers')
    assert media.is_movie() is True


def is_tv_show_media_test():
    media = netflix_roulette.NetflixMedia('The Boondocks')
    assert media.is_tv_show() is True
