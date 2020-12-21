from flask import Flask
from flask import render_template
import urllib.request
import json
import urllib.parse
import os

app = Flask(__name__)
api_key = os.environ.get('WEATHER_KEY')
lat = 35.681
lon = 139.686
weather_api = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang=ja&units=metric&exclude=hourly"


@app.route('/', methods=['GET'])
def weather():
    api_key = os.environ.get('WEATHER_KEY')
    with urllib.request.urlopen(weather_api) as res:
        body = res.read()
        results = json.loads(body)
        data = {
            'location_name': results['name'],
            'daily_temperature': results['main']['temp'],
            'min_temperature': results['main']['temp_min'],
            'max_temperature': results['main']['temp_max'],
            'geo': results['coord'],
            'weather': results['weather'][0]['description'],
            'weather_img': results['weather'][0]['icon'],
        }
        api_url = f"http://api.openweathermap.org/data/2.5/weather?lat=data.geo['lat']&lon=data.geo['lon']&appid={api_key}&lang=ja"
    return render_template('weather.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
