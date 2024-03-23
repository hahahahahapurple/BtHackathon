from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
# init SQLAlchemy so we can use it later in our models

def getFactors():
    factors = []
    for i in range(7):
        item = request.form.get("SOMETHING" + str(i + 1))
        factors.append(item)
    return factors



def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['POST', 'GET'])
    def index():
        if request.method == 'GET':
            return render_template('index.html')
        elif request.method == 'POST':
            getFactors()
            
            


    return app
  
