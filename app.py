import os
from flask import (
    Flask,
    request,
    abort,
    jsonify
)
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Actors, Movies, setup_db
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
                            'Access-Control-Allow-Headers',
                            'Content-Type, Authorization, true'
                            )
        response.headers.add(
                            'Access_Control-Allow-Headers',
                            'GET, POST, DELETE, PATCH, OPTIONS'
                            )
        return response

    QUESTIONS_PER_PAGE = 10

    def pagination(request, selection):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        formated_page = [actor.format() for actor in selection]
        current = formated_page[start:end]

        return current

    # Public user access
    @app.route('/')
    def index():
        return jsonify({
          'success': True,
          'application': 'Casting Agency'
        })

    # Actor Private Access to get all infrmation of actors
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        actors = Actors.query.all()
        formated_actor = pagination(request, actors)

        if len(formated_actor) == 0:
            abort(404)

        return jsonify({
          'success': True,
          'actore': formated_actor,
          'total_actor': len(Actors.query.all())
        })

    # Update actors innformation passed on ID input
    @app.route('/actors/<int:actore_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def update_actors(payload, actore_id):
        actors = Actors.query.filter(Actors.id == actore_id).one_or_none()

        body = request.get_json(force=True)

        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')

        if body is None:
            abort(404)

        actors.name = name
        actors.age = age
        actors.gender = gender
        actors.update()

        return jsonify({
            'success': True,
            'updated': actore_id,
            'actor': [actors.format()],
            'total_actor': len(Actors.query.all())
          })

    # Delete actor basses in ID input
    @app.route('/actors/<int:actore_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actors(payloads, actore_id):
        actore = Actors.query.filter(Actors.id == actore_id).one_or_none()
        if actore is None:
            abort(404)
        actore.delete()

        return jsonify({
            'success': True,
            'delete': actore_id
          })

    # Add ne actor information
    @app.route('/actors/create', methods=['POST'])
    @requires_auth('post:actor')
    def add_actors(payload):
        body = request.get_json(force=True)

        create_name = body.get('name')
        create_age = body.get('age')
        create_gender = body.get('gender')
        actors = Actors(
                      name=create_name,
                      age=create_age,
                      gender=create_gender
                      )
        if create_name == '' or create_age == '' or create_gender == '':
            abort(404)

        actors.insert()
        actor = [Actors.query.get(actors.id).format()]

        return jsonify({
          'success': True,
          'actors': actor
        })

    # Movie Private Access to get all inforaion of actors
    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(payload):
        movies = Movies.query.order_by(Movies.id).all()
        formated_movie = pagination(request, movies)

        if len(formated_movie) == 0:
            abort(404)

        return jsonify({
          'success': True,
          'movie': formated_movie,
          'total_movie': len(Movies.query.all())
        })

    # Add new movie in the list of movies
    @app.route('/movies/create', methods=['POST'])
    @requires_auth('post:movie')
    def add_movies(payload):
        body = request.get_json(force=True)

        create_title = body.get('title')
        create_release_date = body.get('relase_date')

        movies = Movies(
                        title=create_title,
                        relase_date=create_release_date
                        )

        if create_title == '' or create_release_date == '':
            abort(404)

        movies.insert()

        movie = [Movies.query.get(movies.id).format()]

        return jsonify({
            'success': True,
            'movie': movie
            })

    # Update movies information bassed on ID input
    @app.route('/movies/<movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_movie(payload, movie_id):
        movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
        body = request.get_json(force=True)
        title = body.get('title')
        relase_date = body.get('relase_date')

        if title == '' or relase_date == '':
            abort(404)

        movie.title = title
        movie.relase_data = relase_date

        movie.update()
        return jsonify({
          'success': True,
          'updated': movie_id,
          'movie': [movie.format()]
        })

    # Delete Movie based on ID input
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movies(payloads, movie_id):
        movie = Movies.query.filter(Movies.id == movie_id).one_or_none()

        if movie is None:
            abort(404)

        movie.delete()

        return jsonify({
          'success': True,
          'delete': movie_id
        })

    # Handeler Erorr
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
          'success': False,
          'error': 404,
          'message': 'Not Found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
          'success': False,
          'error': 422,
          'message': 'unprocessable'
        }), 422

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
          'success': False,
          'error': error.status_code,
          'message': error.error['description']
          }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
