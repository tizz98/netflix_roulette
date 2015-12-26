import json
from os.path import join, abspath, dirname

from flask import Flask, Response, request


app = Flask(__name__)

with open(abspath(join(dirname(__file__), 'test_data.json')), 'r') as f:
    movie_data = json.load(f)

MEDIA_ERROR = 0
DIRECTOR_ERROR = 1
ACTOR_ERROR = 2


def get_movie(title):
    for movie in movie_data['movies']:
        if movie['show_title'] == title:
            return movie
    return None


def get_error_dict(error_type):
    error_dict = {
        'errorcode': 404,
        'message': '',
    }

    if error_type == MEDIA_ERROR:
        error_dict['message'] = "Sorry! We couldn't " \
                              "find a movie with that title!"
    elif error_type == DIRECTOR_ERROR:
        error_dict['message'] = "Sorry! We couldn't find any " \
                              "movies directed by that director!"
    elif error_type == ACTOR_ERROR:
        error_dict['message'] = "Sorry! We couldn't find " \
                              "any movies with that actor!"

    return error_dict


@app.route('/api/api.php')
def api_route():
    request_args = request.args
    return_status = 200
    return_data = {}

    if request_args.get('title') is not None:
        movie_title = request_args['title']
        year = request_args.get('year')

        movie = get_movie(movie_title)

        if movie is not None:
            if year is not None:
                if movie['release_year'] == year:
                    return_data = movie
                else:
                    return_data = get_error_dict(MEDIA_ERROR)
                    return_status = 404
            else:
                return_data = movie
        else:
            return_data = get_error_dict(MEDIA_ERROR)
            return_status = 404
    elif request_args.get('director') is not None:
        director_name = request_args['director']

        media = movie_data['directors'].get(director_name)

        if media is not None:
            return_data = media
        else:
            return_data = get_error_dict(DIRECTOR_ERROR)
            return_status = 404
    elif request_args.get('actor') is not None:
        actor_name = request_args['actor']

        media = movie_data['actors'].get(actor_name)

        if media is not None:
            return_data = media
        else:
            return_data = get_error_dict(ACTOR_ERROR)
            return_status = 404

    json_data = json.dumps(return_data)
    response = Response(json_data, status=return_status,
                        mimetype='application/json')
    return response


if __name__ == "__main__":
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    app.run()
