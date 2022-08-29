#import your dependenccies
from flask import Flask, jsonify

#define the create ap function
def create_app(test_config=None):
    #create and config the app
    #the parameter__name__ is the name of the current python module
    app = Flask(__name__)

    #@app.route decorator to create an endpoint to path / 
    # and define a function to handle that route.
    @app.route('/')
    def hello():
        return jsonify({'message': 'HELLO WORLD'})

    @app.route('/smiley')
    def smiley():
        return ':)'    

    return app