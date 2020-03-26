from flask import render_template, Flask
from person import Person
from database import *

# Create the application instance
app = Flask(__name__, template_folder='templates')

# Create a URL route in application for "/"
@app.route('/')
def home():
    return render_template('home.html')

# If in stand alone mode, run the application
if __name__ == '__main__':
    db.connect()
    db.create_tables([Person])
    app.run(debug=True)