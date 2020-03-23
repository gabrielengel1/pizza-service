from datetime import date
from flask import render_template, Flask
from peewee import *

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Connecting to MariaDB Docker Image
db = MySQLDatabase('MariaDB', user='root', password='root', host='127.0.0.1', port=3306)

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()
db.create_tables([Person])

uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
uncle_bob.save() # bob is now stored in the database
# Returns: 1

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)