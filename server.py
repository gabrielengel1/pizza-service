from flask import render_template
from database import db
from api import app
from models import create_models

# Create a URL route in application for "/"
@app.route('/')
def home():
    return render_template('home.html')

# If in stand alone mode, run the application
if __name__ == '__main__':
    db.connect()
    create_models()
    app.run(debug=True)