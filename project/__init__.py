from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
# init SQLAlchemy so we can use it later in our models
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
  
