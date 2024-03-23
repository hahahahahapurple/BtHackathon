from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import openai
from openai import OpenAI
# init SQLAlchemy so we can use it later in our models



def create_app():
    app = Flask(__name__)

    app.config['OPENAI_API_KEY'] = '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'


    return app
  
