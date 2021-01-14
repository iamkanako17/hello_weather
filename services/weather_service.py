import urllib.request
import os
import json
from models.weather import Weather

api_key = os.environ.get('WEATHER_KEY')


class WeatherAPI:
    @classmethod
    def get_weather(cls, lat, lon):
        weather_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely&appid={api_key}&units=metric&lang=ja"
        with urllib.request.urlopen(weather_url) as res:
            body = res.read()
            return Weather(json.loads(body))
