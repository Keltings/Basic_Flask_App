#import your dependenccies
import os # to access the os and file structure
from flask import Flask, jsonify

#define the create ap function
def create_app(test_config=None):
    #create and config the app
    #the parameter__name__ is the name of the current python module
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
    SECRET_KEY='dev', 
    #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    #@app.route decorator to create an endpoint to path / 
    # and define a function to handle that route.
    @app.route('/')
    def hello():
        #Instead of returning text, use jsonify to send an 
        # object containing the message
        return jsonify({'message': 'HELLO WORLD'})

    @app.route('/smiley')
    def smiley():
        return ':)'    

    return app