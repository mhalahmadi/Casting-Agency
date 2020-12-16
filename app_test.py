import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movies

casting_assistant = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZLci1RdFhjR01SaVZqdVVXb3JmaSJ9.eyJpc3MiOiJodHRwczovL2Rldi1taXJhaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZkOTJjY2UyOWZkNGUwMDc2ODlhNWJmIiwiYXVkIjoiQ2FzdGluZ0FnZW5jeSIsImlhdCI6MTYwODEwMTMwNiwiZXhwIjoxNjA4MTA4NTA2LCJhenAiOiJxTjZjeU5mcXNQcmVxb1FXaHZZRHg2QWNDdGlnWE12NiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.oCc_MhHWX1-nz09QEgNsGLSeI29dNJ8iHEFlkU6515IMvwv5lVPcPqpZsY0-KujQPlQJAn3ZTWo5k1lLhrvxhxByUtBDvjp71qnKJK_S1xAMztCoy9RaC0wA4pb3_WDm9mELc8o67BUKSJh4tbkcNQIEstmKB0vyUFvMOHVgYoz46vkfCkSGEVH6j6wLoUuqGKAWldXICAXuJa42KSUPC_knTiWuF_yktDklO7hPAb2l-I0BuOPf40tN7XhNYpaNinzktfQ6lCkWc3mqWGgXX-WBrfXBai2q2AoAMlZxvKVW4mRJt7IyNzoTRx67KfP7zKHnmGQdds-Ber31iZcgfg'
casting_director = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZLci1RdFhjR01SaVZqdVVXb3JmaSJ9.eyJpc3MiOiJodHRwczovL2Rldi1taXJhaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZkOTA5NGI5MzFlMDIwMDZmMzY3ZmU2IiwiYXVkIjoiQ2FzdGluZ0FnZW5jeSIsImlhdCI6MTYwODEwMTU5MywiZXhwIjoxNjA4MTA4NzkzLCJhenAiOiJxTjZjeU5mcXNQcmVxb1FXaHZZRHg2QWNDdGlnWE12NiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBvc3Q6YWN0b3IiXX0.PWrEAzaRYatxMc9xBEcq3RtCyq2HcxVz7DyVCSyigxGxPh681AZ6LWoxKpNHPn51bDlIwH9ynZgAMFY7cRGlYjCmGx2aVdL0ABqFz2H83JGXh4VreT89hc_zcH1bSvyXPBz9yrPy1jJoxHNP6fg-oyGwKZQGm1v-6t9q-CJ9HrVnP4U6QX5mQb3ZidYqwlfqFl5Qx41hv7xpqzDdVdo0nTiP68K2IlIdT5_IGYrZE_9VHjIlzf0XzeJIWVJiOXsDF-nHZJpIDogLPOwqO0rJ9LgERwU1PFdDtw_vMfJTkJ1LcwjFZRmZGJv9w7yT9U5pMhdvykZwre_-SZNKhhpyPA'
casting_executive = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZLci1RdFhjR01SaVZqdVVXb3JmaSJ9.eyJpc3MiOiJodHRwczovL2Rldi1taXJhaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZkOTA3MmE2ZTBmZmUwMDc1ZGFlNTlkIiwiYXVkIjoiQ2FzdGluZ0FnZW5jeSIsImlhdCI6MTYwODEwODMxMiwiZXhwIjoxNjA4MTE1NTEyLCJhenAiOiJxTjZjeU5mcXNQcmVxb1FXaHZZRHg2QWNDdGlnWE12NiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.ccEGorDaJwmRa_HV7oozOtwOcIrRy7zuHKEOUijhVRZvD_8fBgs7U4LspAHUrOZxJKCU6siSNWf6PNejLgKY0WOPLxuUPAzCqpjjr5Uea5OExq-lnzfTm36Bi0LyLyLsWpsywQy1QfxSvSRYbHbBy9oyNAT2SgJqTqkwPqfe9gLZkGsMarIrAsWca8pjz_0rpGRGQUpqOjFPpDpWt7L0_1Qw_nLodc3zPJeaDAElJfVkNxe12u79CWVrpHsunnCVnQJ4HIB7mYa_MWVGU17DtmHRWWX4HuSanbcLJNNULhrJ6deSsUW9zmmHtWbBpRvPP46oQ2N8vWGiUzzXgLkeJw'

class CastingAgencyTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = "postgresql://{}@{}/{}".format('postgres','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.new_actor={
            'name': 'mona',
            'age': '22',
            'gender': 'female'
        }

        self.actore={
            'name': 'adam',
            'age': '12',
            'gender': 'm'
        }

        self.update_actore={
            'name': 'mona',
            'age': '22',
            'gender': 'f' 
        }

        self.actore2={
            'name':"ahmed",
            'age': '22',
            'gender': 'm'
        }

        self.update_actore2={
            'name': 'salem',
            'age': '',
        }

        self.delete_actore={
            'name':'mona',
            'age': '22',
            'gender': 'f'
        }

        self.movie={
            'title':'new hero',
            'relase_date': '2020/12/12 12:12:12'
        }

        self.movie2={
            'title': 'new one',
            'relase_date': '2020/12/12 10:10:12'
        }

        self.update_movie={
            'title': 'new hero',
            'relase_date': '2020/12/12 10:10:10'
        }

        self.error_update_movie={
            'title':'s',
            'relase_data': '12020/01/03 12:12:32'
        }

        self.delete_movie={
            'titele': 'new hero',
            'relase_date': '2020/01/01 : 12:12:12'
        }

        self.error_post_movie={
            'title': ''
        }
        

    def tearDown(self):

        pass

    #---------------------------#
    #------- Actore Test -------#
    #---------------------------#

    def test_get_actore(self):
        res = self.client().get('/actors', headers ={ "Authorization":(casting_executive)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actore']))
        self.assertTrue(data['total_actor'])

    def test_404_get_actore(self):
        res = self.client().get('/actors?page=10000', json = self.new_actor, headers = {'Authorization': (casting_executive)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

    def test_update_actors(self):
        self.client().post('/actors/create', json=self.actore, headers = {'Authorization': (casting_executive)})
        res = self.client().patch('/actors/5', json = self.update_actore, headers = {'Authorization': (casting_executive)})
        data  = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actor']))
        self.assertTrue(data['total_actor'])
    
    def test_error_update_actor(self):
        self.client().post('/actors/create', json=self.actore2, headers = {'Authorization': (casting_executive)})
        res = self.client().patch('/actores/222222', json = self.update_actore2, headers = {'Authorization': (casting_executive)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # def test_delete_actore(self):
    #     res = self.client().delete('/actors/24', json = self.delete_actore, headers = {'Authorization': (casting_executive)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)

    # def test_error_delete_actore(self):
    #     res = self.client().delete('/actores/24', json = self.delete_actore, headers = {'Authorization': (casting_executive)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)

    #------------------------------------#
    #------------- Movie Test -----------#
    #------------------------------------#

    def test_get_movie(self):
        res = self.client().get('/movies' , headers ={'Authorization': (casting_executive)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_error_get_movie(self):
        res = self.client().get('/movies?page=100000', json = self.movie, headers = {'Authorization': (casting_executive)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    
    def test_update_movie(self):
        self.client().post('movies/create', json = self.movie, headers = {'Authorization': (casting_executive)})
        res = self.client().patch('/movies/3', json = self.update_movie, headers = {'Authorization': (casting_executive)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_error_update_movie(self):
        self.client().post('/movies/create', json = self.movie2, headers = {'Authorization': (casting_executive)})
        res = self.client().patch('/movies/555', json = self.error_update_movie, headers = {'Authorization': (casting_executive)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_post_movie(self):
        res = self.client().post('/movies/create', json = self.movie2, headers = {'Authorization': (casting_executive)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_error_post_movie(self):
        res = self.client().post('/movie/create', json = self.error_post_movie, headers = {'Authorization': (casting_executive)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # def test_delete_movie(self):
    #     res = self.client().delete('/movies/14', json = self.delete_movie, headers = {'Authorization': (casting_executive)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)

    # def test_error_delete_mivie(self):
    #     res = self.client().delete('/movies/13', json = self.delete_movie, headers = {'Authorization': (casting_executive)})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)

    #-----------------------------------#   
    #------- Authontication Error-------#
    #-----------------------------------#

    def test_authontaction_error_delete_actore(self):
        res = self.client().delete('/actors/12', json = self.delete_movie, headers = {'Authorization': (casting_assistant)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_authontaction_error_delete_movie(self):
        res = self.client().delete('/actors/12', json = self.delete_movie, headers = {'Authorization': (casting_director)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)




    
    



if __name__ == "__main__":
    unittest.main()


