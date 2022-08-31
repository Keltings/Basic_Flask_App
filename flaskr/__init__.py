from types import NoneType
from flask import Flask, jsonify, request, abort
from models import setup_db, Plant
from flask_cors import CORS, cross_origin

def create_app(test_config=None):
    #Initialization
    app = Flask(__name__, instance_relative_config=True)
    setup_db(app)
    # CORS(app, resources={r"*/api/*" : {origins: '*}})---Resource-Specific Usage
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response


    #@cross_origin
    
    #------------------- get plants and return that information to the user------------
    
    
    @app.route('/plants', methods=['GET', 'POST'])
    def get_plants():

        #the below line of code is what if we wanted to show 10 plants per page
        #---------------------------------------------------
        page = request.args.get('page', 1, type=int)
        # define the plant i want to start with
        start = (page-1) * 10
        end = start + 10
        #-----------------------------------------------------
        plants = Plant.query.all()
        formatted_plants = [plant.format() for plant in plants]
        return jsonify({
            'success': True,

            'plants': formatted_plants[start:end],
            'total_plants': len(formatted_plants)
        })
        

        #---------------------------------------------
        """we want infor about just a specific plant
        within our route we include that variable name"""
        @app.route('/plants/<int:plant_id>')
        def get_specific_plant(plant_id):
            # identify the plant
            plant = Plant.query.filter(Plant.id == plant_id).one_or_none()
            
            if plant is None:
                abort(404)

            else:    
                return jsonify({
                'success': True,
                'plants': plant.format()
                })    


    @app.errorhandler(404)
    def not_found(error):
        return({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404


    @app.errorhandler(422)
    def unprocessable(error):
        return({
            'success': False,
            'error': 422,
            'message': 'unprocessble'
        }), 422


    return app    