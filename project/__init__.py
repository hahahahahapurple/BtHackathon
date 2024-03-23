from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
# init SQLAlchemy so we can use it later in our models
def create_app():
    app = Flask(__name__)

    return app
  
