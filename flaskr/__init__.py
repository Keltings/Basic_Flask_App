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
    @app.route('/')
    def hello_world():
        return jsonify({'message':'HELLO, WORLD!'})
    return app    