from flask import Flask
from flask import render_template
from flask import request
from jinja2 import Markup, escape, Environment
from controllers import weather_controller
import urllib.request
import json
import urllib.parse
import os
import datetime


app = Flask(__name__)
app.register_blueprint(weather_controller.app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
