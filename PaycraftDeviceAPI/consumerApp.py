from flask import Flask
from db import db
from dotenv import load_dotenv
import os

"""Creating an application at Consumer end, to help Consumer fetch data and save further to database."""

consumer_app = Flask(__name__)

load_dotenv(".env") #Loading .env file containing necessary info.

"""Getting the secret_key and database URI from loaded environment file."""
consumer_app.secret_key= os.environ.get("SECRET")
consumer_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI")
consumer_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request  # To be executed before any request and create the necessary tables.
def create_table():
    db.create_all()

"""Initialize database connection."""
db.init_app(consumer_app)

if __name__ == '__main__' :

    consumer_app.run() #Starting application