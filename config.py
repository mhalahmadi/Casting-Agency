import os
SECRET_KEY = os.urandom(32)

basedeir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgresql://postgre@localhost:5432/casting_agencys'