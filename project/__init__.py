from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
# init SQLAlchemy so we can use it later in our models

def getNums():
    nums = []
    for i in range(7):
        item = request.form.get("SOMETHING" + str(i + 1))
        nums.append(item)
    return nums



def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['POST', 'GET'])
    def index():
        if request.method == 'GET':
            return render_template('index.html')
        elif request.method == 'POST':
            factors = ["1","1","1","1","1","1","1"]
            paragraph = "I am going to give you a list of critera for songs. Here are the criteria:"
            nums = getNums()
            for i in range(7):
                paragraph += (factors[i] + ": " + str(nums[i]))
            print(paragraph)


            
            


    return app
  
