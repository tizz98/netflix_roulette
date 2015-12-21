# coding=utf-8
import netflix_roulette


def simple_movie_test():
    media = netflix_roulette.NetflixMedia('The Avengers')
    assert media.is_on_netflix is True


def movietype_test():
    media = netflix_roulette.NetflixMedia('The Boondocks')
    assert media.get_readable_mediatype() == 'TV Show'


def movie_test_with_year_test():
    media = netflix_roulette.NetflixMedia('The Boondocks', year=2005)
    assert media.year == 2005


def unicode_title_test():
    # Make sure unicode is properly encoded
    media = netflix_roulette.NetflixMedia(u'H βουλευτινα')
