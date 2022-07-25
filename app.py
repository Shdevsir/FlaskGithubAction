from flask import Flask
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class SecretPhrase(Resource):
    def get(self):
        question = os.environ.get("QUESTION")
        answer = os.environ.get("ANSWER")
        return {question: answer}


api.add_resource(HelloWorld, '/')
api.add_resource(SecretPhrase, '/secret')

if __name__ == '__main__':
    app.run(debug=True)
