from flask import Flask, render_template, url_for, redirect, request, flash
import os

@main.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
