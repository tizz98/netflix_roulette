# coding=utf-8
import netflix_roulette


netflix_roulette.Request._base_url = 'http://127.0.0.1:5000/api/api.php'


def test_director_name():
    director = netflix_roulette.NetflixDirector('Quentin Tarantino')
    assert director.name == 'Quentin Tarantino'
    assert director.is_on_netflix is True


def test_director_movies():
    director = netflix_roulette.NetflixDirector('Quentin Tarantino')
    assert director.media is not None and director.media is not []

    for media in director.media:
        assert isinstance(media, netflix_roulette.NetflixMedia)
        assert media._data_set is True


def test_director_not_on_netflix():
    director = netflix_roulette.NetflixDirector('Quinten Tarentino')
    assert director.media == []
    assert director.is_on_netflix is False


def test_actor_name():
    actor = netflix_roulette.NetflixActor('Nicolas Cage')
    assert actor.name == 'Nicolas Cage'


def test_actor_movies():
    actor = netflix_roulette.NetflixActor('Nicolas Cage')
    assert actor.media is not None and actor.media is not []

    for media in actor.media:
        assert isinstance(media, netflix_roulette.NetflixMedia)
        assert media._data_set is True
