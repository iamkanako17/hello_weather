from flask import Flask
from flask import render_template
from flask import request
from jinja2 import Markup, escape, Environment
from flask.blueprints import Blueprint
from services.weather_service import WeatherAPI
import urllib.request
import json
import urllib.parse
import os
import datetime

app = Blueprint('weather', __name__)


@app.route('/weather', methods=['POST'])
def weather():
    lat = request.form.get('latitude')
    lon = request.form.get('longitude')

    try:
        weather = WeatherAPI.get_weather(lat, lon)
        return render_template('weather.html', weather=weather)
    except urllib.error.HTTPError as e:
        message = "天気情報取得中にエラーが発生しました。"
        print(e)
        return render_template('error.html', message=message)
    except Exception as e:
        message = "何らかのエラーが起きました。"
        print(e)
        return render_template('error.html', message=message)


@app.app_template_filter('format_date')
def format_date(value, format="%m/%d(%a) %H:%M"):
    return datetime.datetime.fromtimestamp(value).strftime(format)
