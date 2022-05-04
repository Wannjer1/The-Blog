from flask import Flask 
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):


    # initializing application
    app = Flask(__name__,instance_relative_config=True)

    # creating the app configurations

    # initializing Flask extension
