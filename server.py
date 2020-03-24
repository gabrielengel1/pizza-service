from flask import render_template, Flask
from database import *

# Create the application instance
app = Flask(__name__, template_folder='templates')

# Create a URL route in application for "/"
@app.route('/')
def home():
    return render_template('home.html')

# If in stand alone mode, run the application
if __name__ == '__main__':
    connect_db()
    app.run(debug=True)