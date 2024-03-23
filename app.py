from flask import Flask, render_template, url_for, redirect, flash
from project import main
import os

app = Flask(__name__)

app = create_app()
app.secret_key = os.urandom(12)
date = '2024/3/23'

@app.route('/')
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=81,debug = True)
