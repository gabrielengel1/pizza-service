from datetime import date
from flask_restx import Api, Resource
from peewee import *
from database import BaseModel

class Person(BaseModel):
    name = CharField()
    birthday = DateField()

def __init__(self):
    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
    uncle_bob.save() # bob is now stored in the database

@api.route("/person")
@api.doc(params={})
def get_all():
    pass

@api.route("/person/{name}")
@api.doc(params={name})
def get_one(name):
    pass

@api.route("/person")
@api.doc(params={})
def post(person):
    pass

@api.route("/person")
@api.doc(params={})
def update(person):
    pass

@api.route("/person")
@api.doc(params={})
def delete(person):
    pass