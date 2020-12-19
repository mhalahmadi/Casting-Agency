import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
import datetime
import json

DATABASE_URL = os.getenv('DATABASE_URL')

db = SQLAlchemy()


def setup_db(app, database_path=DATABASE_URL):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()


# Movies Table
class Movies(db.Model):
    __tablename__ = 'Movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    relase_date = db.Column(db.DateTime())

    def __init__(self, title, relase_date):
        self.title = title,
        self.relase_date = relase_date

    def format(self):
        return{
            'id': self.id,
            'title': self.title,
            'relase_date': self.relase_date
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

# Actors Table
class Actors(db.Model):
    __tablename__ = 'Actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    age = db.Column(db.String(120))
    gender = db.Column(db.String(120))

    # def __init__(self, name, age, gender):
    #     self.id = id,
    #     self.name = name,
    #     self.age = age,
    #     self.gender = gender

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        