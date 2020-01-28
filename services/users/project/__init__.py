# services/users/project/__init__.py

from flask import Flask, jsonify
from flask_restful import Resource, Api

# instance of app
app = Flask(__name__)
api = Api(app)

# set config
app.config.from_object('project.config.DevelopmentConfig')

class UserPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'Pong!'
        }

api.add_resource(UserPing, '/user/ping/')
