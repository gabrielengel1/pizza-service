from person import Person
from database import db

def create_models():
    db.create_tables([Person])