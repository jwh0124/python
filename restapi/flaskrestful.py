from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

CORS(app, resources={r'*': {'origins': '*'}})

class TestRestApi(Resource) :
    def get(self) :
        return {'result': True, 'score': 60}

api.add_resource(TestRestApi, '/test')

if __name__ == '__main__':
    app.run(debug=True)