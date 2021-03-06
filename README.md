# Netflix Roulette
This is a simple python wrapper for the [Netflix Roulette API](http://netflixroulette.net/api/).

[![Build Status](https://travis-ci.org/tizz98/netflix_roulette.svg?branch=master)](https://travis-ci.org/tizz98/netflix_roulette)
[![PyPI version](https://img.shields.io/pypi/v/netflix_roulette.svg)](https://pypi.python.org/pypi/netflix_roulette)
[![Python Versions](https://img.shields.io/pypi/pyversions/netflix_roulette.svg)](https://pypi.python.org/pypi/netflix_roulette)
[![License](https://img.shields.io/pypi/l/netflix_roulette.svg)](https://github.com/tizz98/netflix_roulette/blob/master/LICENSE.md)
[![Code Climate](https://codeclimate.com/github/tizz98/netflix_roulette/badges/gpa.svg)](https://codeclimate.com/github/tizz98/netflix_roulette)

## Installation
#### Pip
- `pip install netflix_roulette`

#### From Source
- `git clone git@github.com:tizz98/netflix_roulette.git`
- `cd netflix_roulette`
- `python setup.py install`

## Usage
#### Simple Query
```python
>>> import netflix_roulette
>>> media = netflix_roulette.NetflixMedia('Attack on titan')
>>> media
<NetflixMedia(title='Attack on titan', year='None')>
>>> media.show_id
70299043
>>> media.summary
u'For over a century, people have been living behind barricades to block out the giant Titans that threaten to destroy the human race. When a Titan destroys his hometown, young Eren Yeager becomes determined to fight back.'
>>> media.is_on_netflix
True
>>> media.get_readable_mediatype()
'TV Show'
```

#### Query with year
```python
>>> import netflix_roulette
>>> media = netflix_roulette.NetflixMedia('The Boondocks', year=2005)
>>> media
<NetflixMedia(title='The Boondocks', year='2005')>
>>> media.show_id
70153391
>>> media.summary
u'Based on the comic strip by Aaron McGruder, this satirical animated series follows the socially conscious misadventures of Huey Freeman, a preternaturally smart 10-year-old who relocates from inner-city Chicago to the suburbs.'
>>> media.is_on_netflix
True
>>> media.get_readable_mediatype()
'TV Show'
```

## `class NetflixMedia`

#### Parameters
- `title`: Title of the media you are searching for.
- `year`: (Optional) Year of the media you are searching for.

#### Attributes
- `title`: User supplied title of the media you are searching for.
- `year`: User supplied year of the media you are searching for.
- `rating`: How high the media is rated, max is 5.
- `poster`: The poster for the media, right from the Netflix CDN.
- `mediatype`: 0 means movie, 1 means TV Show. See also `get_readable_mediatype()`.
- `release_year`: The media's release date.
- `show_cast`: The cast of a given title.
- `category`: A title's given category.
- `summary`: A plot summary.
- `director`: The name(s) of the director(s) of a given title.
- `show_id`: The Netflix id of the title.
- `is_on_netflix`: A boolean, whether or not the show is on Netflix.

#### Methods
- `get_readable_mediatype()`: Returns `TV Show` or `Movie` instead of `1` or `0`.
- `is_movie()`: Returns `True` if the media is a Movie.
- `is_tv_show()`: Returns `True` if the media is a TV Show.


## `class NetflixDirector`

#### Parameters
- `name`: Name of the director you are searching for.

#### Attributes
- `name`: User supplied name.
- `media`: List of `NetflixMedia` that the person has directed.


## `class NetflixActor`

#### Parameters
- `name`: Name of the actor you are searching for.

#### Attributes
- `name`: User supplied name.
- `media`: List of `NetflixMedia` that the person has been in.
