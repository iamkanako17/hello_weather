from flask import Flask
from flask import render_template
from flask import request
from jinja2 import Markup, escape, Environment
import urllib.request
import json
import urllib.parse
import os
import datetime
import re
import jinja2


app = Flask(__name__)
api_key = os.environ.get('WEATHER_KEY')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    lat = request.form.get('latitude')
    lon = request.form.get('longitude')

    weather_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely&appid={api_key}&units=metric&lang=ja"
    try:
        with urllib.request.urlopen(weather_url) as res:
            body = res.read()
            results = json.loads(body)
            hourly_weather = results['hourly'][1:5]
            daily_weather = results['daily'][1:8]
            data = {
                'timezone': results['timezone'],
                'now_time': datetime.datetime.fromtimestamp(results['current']['dt']),
                'now_temperature': results['current']['temp'],
                'now_weather': results['current']['weather'][0]['description'],
                'now_humidity': results['current']['humidity'],
                'now_wind': results['current']['wind_speed'],
                'now_weather_img': results['current']['weather'][0]['icon']
            }
        return render_template('weather.html', data=data, daily_weather=daily_weather, hourly_weather=hourly_weather)
    except urllib.error.HTTPError as e:
        message = "天気情報取得中にエラーが発生しました。"
        print(e)
        return render_template('error.html', message=message)
    except Exception as e:
        message = "何らかのエラーが起きました。"
        print(e)
        return render_template('error.html', message=message)


loader = jinja2.FileSystemLoader('/templates')
environment = jinja2.Environment(autoescape=True, loader=loader)


@app.template_filter('format_date')
def format_date(daily_weather, format="%m/%d(%a)"):
    return datetime.datetime.fromtimestamp(daily_weather).strftime(format)


environment.filters['format_date'] = format_date


@app.template_filter('format_hour')
def format_hour(hourly_weather, format='%H:%M'):
    return datetime.datetime.fromtimestamp(hourly_weather).strftime(format)


environment.filters['format_hour'] = format_hour


if __name__ == "__main__":
    app.run(debug=True)
