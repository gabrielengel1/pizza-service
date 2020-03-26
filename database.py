from peewee import *

# Initialising Database & Connecting to MariaDB Docker
db = MySQLDatabase('homestead', user='root', password='root', host='127.0.0.1', port=3306)

class BaseModel(Model):
    class Meta:
        database = db # This model uses the "people.db" database.