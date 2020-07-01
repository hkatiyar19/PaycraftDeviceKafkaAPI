from flask import Flask
from flask_jwt_extended import JWTManager
from db import db
from flask_restful import Api
from PaycraftDeviceAPI.resources.DeviceRegister import DeviceRegister
from PaycraftDeviceAPI.resources.Login import Login
from PaycraftDeviceAPI.resources.DeviceUsage import DeviceAvgUsage
from dotenv import load_dotenv
import os


"""Creating Client side application to get messages through api endpoints and send further to Kafka broker through producer."""

app =Flask(__name__) 

load_dotenv(".env") #Loading .env file containing necessary info.

"""Getting the secret_key and database URI from loaded environment file."""
consumer_app.secret_key= os.environ.get("SECRET")
consumer_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI")
consumer_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWTManager(app) # Create jwt object for authentication handling.
api = Api(app)

@app.before_first_request  # To be executed before any request and create the necessary tables.
def create_table():
    db.create_all()
    
"""Mapping resources to endpoints."""
api.add_resource(DeviceRegister,'/devices/register')
api.add_resource(DeviceAvgUsage,'/devices/<string:dev_id>/cpu_usage')
api.add_resource(Login,'/login')

if __name__ == '__main__' :
    db.init_app(app)
    app.run(debug=True) # Starting Client Side application.

