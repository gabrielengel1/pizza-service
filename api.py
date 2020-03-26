from flask import Flask
from flask_restx import Api

#Idea - not yet finished
"""
class Api:
    def __init__(self, app):
        self.app
        self.route_doc = {}

    def route(self, path):
        def wrapper(fn):
        self.route_doc(fn) = {}
        return self.app.route(fn.path)

    def doc(self, **kwargs):
        def wrapper(fn):
            self.route_doc(fn) = kwargs
            return fn
        return wrapper
"""

app = Flask(__name__, template_folder='templates')
api = Api(app)