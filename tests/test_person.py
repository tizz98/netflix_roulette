# coding=utf-8
import netflix_roulette


def test_director_name():
    director = netflix_roulette.NetflixDirector('Quentin Tarantino')
    assert director.name == 'Quentin Tarantino'


def test_director_movies():
    director = netflix_roulette.NetflixDirector('Quentin Tarantino')
    assert director.media is not None and director.media is not []

    for media in director.media:
        assert isinstance(media, netflix_roulette.NetflixMedia)
        assert media._data_set is True


def test_actor_name():
    actor = netflix_roulette.NetflixActor('Nicolas Cage')
    assert actor.name == 'Nicolas Cage'


def test_actor_movies():
    actor = netflix_roulette.NetflixActor('Nicolas Cage')
    assert actor.media is not None and actor.media is not []

    for media in actor.media:
        assert isinstance(media, netflix_roulette.NetflixMedia)
        assert media._data_set is True
