# Netflix Roulette
This is a simple python wrapper for the [Netflix Roulette API](http://netflixroulette.net/api/).

## Installation
- `git clone git@github.com:tizz98/netflix_roulette.git`
- `cd netflix_roulette`
- `python setup.py install`

## Usage
#### Simple Query
```python
import netflix_roulette

media = netflix_roulette.NetflixMedia('Attack on titan')
```

#### Query with year
```python
import netflix_roulette

media = netflix_roulette.NetflixMedia('The Boondocks', year=2005)
```

## `class NetflixMedia`

#### Parameters
- `title`: Title of the media you are searching for.
- `year`: (Optional) Year of the media you are searching for.

#### Attributes
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
