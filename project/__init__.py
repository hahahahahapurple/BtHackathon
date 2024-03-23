from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from authlib.integrations.flask_client import OAuth
import os
# init SQLAlchemy so we can use it later in our models
def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    app.secret_key = os.urandom(12)

    login_manager = LoginManager()
    login_manager.init_app(app)

    
    with app.app_context():

      # blueprint for auth routes in our app
  
      # blueprint for non-auth parts of app
      from ..project.main import main as main_blueprint
      app.register_blueprint(main_blueprint)
  

    return app
  
