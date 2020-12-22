from flask import Flask
from flask import render_template
import urllib.request
import json
import urllib.parse
import os
import datetime


app = Flask(__name__)
api_key = os.environ.get('WEATHER_KEY')
lat = 35.681
lon = 139.686
weather_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=daily&appid={api_key}&units=metric&lang=ja"


@app.route('/', methods=['GET'])
def weather():
    with urllib.request.urlopen(weather_url) as res:
        body = res.read()
        results = json.loads(body)
        time = datetime.datetime.fromtimestamp
        data = {
            'timezone': results['timezone'],
            'lat': results['lat'],
            'lon': results['lon'],
            'lon': results['lon'],
            'now_time': time(results['current']['dt']),
            'now_temperature': results['current']['temp'],
            'now_weather': results['current']['weather'][0]['description'],
            'now_weather_img': results['current']['weather'][0]['icon'],
            'one_hour_later_time': time(results['hourly'][1]['dt']),
            'two_hour_later_time': time(results['hourly'][2]['dt']),
            'three_hour_later_time': time(results['hourly'][3]['dt']),
            'four_hour_later_time': time(results['hourly'][4]['dt']),
            'one_hour_later_temp': results['hourly'][1]['temp'],
            'two_hour_later_temp': results['hourly'][2]['temp'],
            'three_hour_later_temp': results['hourly'][3]['temp'],
            'four_hour_later_temp': results['hourly'][4]['temp'],
        }
        api_url = f"https://api.openweathermap.org/data/2.5/onecall?lat=data.lat&lon=data.lon&exclude=daily&appid={api_key}&units=metric&lang=ja"
    return render_template('weather.html', data=data, results=results)


if __name__ == "__main__":
    app.run(debug=True)
