from peewee import *
from person import Person

# Initialising Database & Connecting to MariaDB Docker
db = MySQLDatabase('homestead', user='root', password='root', host='127.0.0.1', port=3306)

def connect_db():
    # Connect to MariaDB
    db.connect()
    db.create_tables([Person])

class BaseModel(Model):
    class Meta:
        database = db # This model uses the "people.db" database.