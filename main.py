from flask import Blueprint, render_template

@main.route('/')
def index():
    return render_template('index.html')
