# coding=utf-8
import netflix_roulette


def director_name_test():
    director = netflix_roulette.NetflixDirector('Quentin Tarantino')
    assert director.name == 'Quentin Tarantino'


def director_movies_test():
    director = netflix_roulette.NetflixDirector('Quentin Tarantino')
    assert director.media is not None and director.media is not []

    for media in director.media:
        assert isinstance(media, netflix_roulette.NetflixMedia)
        assert media._data_set is True


def actor_name_test():
    actor = netflix_roulette.NetflixActor('Nicolas Cage')
    assert actor.name == 'Nicolas Cage'


def actor_movies_test():
    actor = netflix_roulette.NetflixActor('Nicolas Cage')
    assert actor.media is not None and actor.media is not []

    for media in actor.media:
        assert isinstance(media, netflix_roulette.NetflixMedia)
        assert media._data_set is True
