from datetime import date
from flask_restx import Resource
from peewee import *
from database import BaseModel
from api import api

@api.route("/person")
@api.doc(params={})
class Person(BaseModel, Resource):
    name = CharField()
    birthday = DateField()

def __init__(self):
    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
    uncle_bob.save() # bob is now stored in the database

@api.doc(params={})
def get_person():
    pass