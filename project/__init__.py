from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import openai
from openai import OpenAI
# init SQLAlchemy so we can use it later in our models

def getNums():
    nums = []
    for i in range(7):
        item = request.form.get("SOMETHING" + str(i + 1))
        nums.append(item)
    return nums



def create_app():
    app = Flask(__name__)

    app.config['OPENAI_API_KEY'] = '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'


    return app
  
