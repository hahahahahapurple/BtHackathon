from flask import Flask, jsonify

# Assume app is initialized in the __init__.py file.
from . import create_app

app = create_app()

@app.route('/')
def hello_world():
    return 'Hello, World!'