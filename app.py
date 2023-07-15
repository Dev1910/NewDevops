from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Define a resource for your API endpoint
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

# Add the resource to the API with a specific route
api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run()
