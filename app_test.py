import os 
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actors, Movies

ASISTANT = "Bearer {}".format(os.environ.get('ASISTANT'))
EXECUTIVE = "Bearer {}".format(os.environ.get('EXECUTIVE'))
UNAUTH = os.environ.get('UNAUTH')
DIRECTOR = "Bearer {}".format(os.environ.get('DIRECTOR'))


class CastingAgencyTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        # self.database_path = os.environ.get('DATABASE_TEST_URl')
        self.database_name = "casting_agency_test"
        self.database_path = "postgresql://{}@{}/{}".format('postgres',
                                                            'localhost:5432',
                                                            self.database_name
                                                            )
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # self.db.drop_all()
            self.db.create_all()

        self.new_actor = {
            'name': 'Emms Robert',
            'age': '29',
            'gender': 'Female'
        }

        self.actore = {
            'name': 'Jennifer Aniston',
            'age': '51',
            'gender': 'Female'
        }

        self.update_actore = {
            'name': 'Will Smith',
            'age': '52',
            'gender': 'Male'
        }

        self.actore2 = {
            'name': "Jason Bateman",
            'age': '51',
            'gender': 'Male'
        }

        self.update_actore2 = {
            'name': 'Adam',
            'age': '',
        }

        self.delete_actore = {
            'name': 'Jennifer Aniston',
            'age': '51',
            'gender': 'Female'
        }

        self.error_post_actor = {
            'name': '',
            'age': '',
            'gender': ''
        }

        self.movie = {
            'title': 'Wild Child',
            'relase_date': '2008/08/10 12:12:12'
        }

        self.movie2 = {
            'title': 'Life Of Crime',
            'relase_date': '2014/08/08 08:10:12'
        }

        self.update_movie = {
            'title': 'Hancock',
            'relase_date': '2008/01/01 11:00:00'
        }

        self.error_update_movie = {
            'title': '',
            'relase_data': ''
        }

        self.delete_movie = {
            'titele': 'Wils Child',
            'relase_date': '2008/08/10 : 12:12:12'
        }

        self.error_post_movie = {
            'title': '',
            'relase_date': ''
        }

    def tearDown(self):

        pass

        # ---------------------------#
        # ------- Actore Test -------#
        # ---------------------------#

    def test_get_actore(self):
        res = self.client().get('/actors',
                                headers={'Authorization': ASISTANT}
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actore']))
        self.assertTrue(data['total_actor'])

    def test_404_get_actore(self):
        res = self.client().get('/actor?page=1000000',
                                headers={'Authorization': DIRECTOR}
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

    def test_post_actor(self):
        res = self.client().post('/actors/create',
                                 json=self.actore,
                                 headers={'Authorization': DIRECTOR}
                                 )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_error_post_actor(self):
        res = self.client().post('/actors/create',
                                 json=self.error_post_actor,
                                 headers={'Authorization': DIRECTOR}
                                 )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_update_actors(self):
        self.client().post('/actors/create',
                           json=self.actore,
                           headers={'Authorization': DIRECTOR}
                           )
        res = self.client().patch('/actors/4',
                                  json=self.update_actore,
                                  headers={'Authorization': DIRECTOR}
                                  )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actor']))
        self.assertTrue(data['total_actor'])

    def test_error_update_actor(self):
        self.client().post('/actors/create',
                           json=self.actore2,
                           headers={'Authorization': DIRECTOR}
                           )
        res = self.client().patch('/actores/222222',
                                  json=self.update_actore2,
                                  headers={'Authorization': DIRECTOR}
                                  )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_actore(self):
        res = self.client().delete('/actors/2',
                                   json=self.delete_actore,
                                   headers={'Authorization': EXECUTIVE}
                                   )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_error_delete_actore(self):
        res = self.client().delete('/actores/2',
                                   json=self.delete_actore,
                                   headers={'Authorization': EXECUTIVE}
                                   )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # # ------------------------------------#
    # # ------------- Movie Test -----------#
    # # ------------------------------------#

    def test_get_movie(self):
        res = self.client().get('/movies',
                                headers={'Authorization': ASISTANT}
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_error_get_movie(self):
        res = self.client().get('/movies?page=100000',
                                json=self.movie,
                                headers={'Authorization': ASISTANT}
                                )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_update_movie(self):
        self.client().post('movies/create',
                           json=self.movie,
                           headers={'Authorization': EXECUTIVE}
                           )
        res = self.client().patch('/movies/2',
                                  json=self.update_movie,
                                  headers={'Authorization': EXECUTIVE}
                                  )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_error_update_movie(self):
        self.client().post('/movies/create',
                           json=self.movie2,
                           headers={'Authorization': EXECUTIVE}
                           )
        res = self.client().patch('/movies/888888',
                                  json=self.error_update_movie,
                                  headers={'Authorization': EXECUTIVE}
                                  )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_post_movie(self):
        res = self.client().post('/movies/create', json=self.movie, headers={'Authorization': EXECUTIVE})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_error_post_movie(self):
        res = self.client().post('/movies/create',
                                 json=self.error_post_movie,
                                 headers={'Authorization': EXECUTIVE}
                                 )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_movie(self):
        res = self.client().delete('/movies/1',
                                   json=self.delete_movie,
                                   headers={'Authorization': EXECUTIVE}
                                   )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_error_delete_movie(self):
        res = self.client().delete('/movies/1',
                                   json=self.delete_movie,
                                   headers={'Authorization': EXECUTIVE}
                                   )

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    # # -----------------------------------#
    # # ------- Authontication Error-------#
    # # -----------------------------------#

    def test_auth_error_post_actore(self):
        res = self.client().post('/actors/create',
                                 json=self.new_actor,
                                 headers={'Authorization': UNAUTH}
                                 )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_auth_error_post_movie(self):
        res = self.client().post('/movies/create',
                                 json=self.movie,
                                 headers={'Authorization': UNAUTH}
                                 )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


if __name__ == "__main__":
    unittest.main()
