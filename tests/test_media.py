# coding=utf-8
import netflix_roulette
from netflix_roulette.constants import TV_SHOW_STR, MOVIE_STR


# Note: testing with specific media will prove to not be reliable
def test_on_netflix_movie():
    media = netflix_roulette.NetflixMedia('The Avengers')
    assert media.is_on_netflix is True


def test_not_on_netflix_movie():
    media = netflix_roulette.NetflixMedia('Home', year=2015)
    print(media.__dict__)
    assert media.is_on_netflix is False


def test_movietype_tv_show():
    media = netflix_roulette.NetflixMedia('The Boondocks')
    assert media.get_readable_mediatype() == TV_SHOW_STR


def test_movietype_movie():
    media = netflix_roulette.NetflixMedia('The Avengers')
    assert media.get_readable_mediatype() == MOVIE_STR


def test_movie_with_year():
    media = netflix_roulette.NetflixMedia('The Boondocks', year=2005)
    assert media.year == 2005


def test_unicode_title():
    # Make sure unicode is properly encoded
    media = netflix_roulette.NetflixMedia('H βουλευτινα')


def test_is_movie_func():
    assert callable(netflix_roulette.NetflixMedia.is_movie)


def test_is_tv_show_func():
    assert callable(netflix_roulette.NetflixMedia.is_tv_show)


def test_is_movie_media():
    media = netflix_roulette.NetflixMedia('The Avengers')
    assert media.is_movie() is True


def test_is_tv_show_media():
    media = netflix_roulette.NetflixMedia('The Boondocks')
    assert media.is_tv_show() is True
