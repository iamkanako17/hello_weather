from flask import Flask
from flask import render_template
from flask import request
import urllib.request
import json
import urllib.parse
import os
import datetime


app = Flask(__name__)
api_key = os.environ.get('WEATHER_KEY')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    lat = request.form.get('latitude')
    lon = request.form.get('longitude')
    weather_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=daily&appid={api_key}&units=metric&lang=ja"
    try:
        with urllib.request.urlopen(weather_url) as res:
            body = res.read()
            results = json.loads(body)
            time = datetime.datetime.fromtimestamp
            data = {
                'timezone': results['timezone'],
                'now_time': time(results['current']['dt']),
                'now_temperature': results['current']['temp'],
                'now_weather': results['current']['weather'][0]['description'],
                'now_humidity': results['current']['humidity'],
                'now_wind': results['current']['wind_speed'],
                'now_weather_img': results['current']['weather'][0]['icon'],
                'one_hour_later_time': time(results['hourly'][1]['dt']),
                'two_hour_later_time': time(results['hourly'][2]['dt']),
                'three_hour_later_time': time(results['hourly'][3]['dt']),
                'four_hour_later_time': time(results['hourly'][4]['dt']),
                'one_hour_later_temp': results['hourly'][1]['temp'],
                'two_hour_later_temp': results['hourly'][2]['temp'],
                'three_hour_later_temp': results['hourly'][3]['temp'],
                'four_hour_later_temp': results['hourly'][4]['temp'],
                'one_hour_later_description': results['hourly'][1]['weather'][0]['description'],
                'two_hour_later_description': results['hourly'][2]['weather'][0]['description'],
                'three_hour_later_description': results['hourly'][3]['weather'][0]['description'],
                'four_hour_later_description': results['hourly'][4]['weather'][0]['description'],
                'one_hour_later_image': results['hourly'][1]['weather'][0]['icon'],
                'two_hour_later_image': results['hourly'][2]['weather'][0]['icon'],
                'three_hour_later_image': results['hourly'][3]['weather'][0]['icon'],
                'four_hour_later_image': results['hourly'][4]['weather'][0]['icon'],
                'probability_of_rain_1': results['hourly'][1]['pop'],
                'probability_of_rain_2': results['hourly'][2]['pop'],
                'probability_of_rain_3': results['hourly'][3]['pop'],
                'probability_of_rain_4': results['hourly'][4]['pop'],
                'one_hour_later_humidity': results['hourly'][1]['humidity'],
                'two_hour_later_humidity': results['hourly'][2]['humidity'],
                'three_hour_later_humidity': results['hourly'][3]['humidity'],
                'four_hour_later_humidity': results['hourly'][4]['humidity'],
                'one_hour_later_wind': results['hourly'][1]['wind_speed'],
                'two_hour_later_wind': results['hourly'][2]['wind_speed'],
                'three_hour_later_wind': results['hourly'][3]['wind_speed'],
                'four_hour_later_wind': results['hourly'][4]['wind_speed']
            }
        return render_template('weather.html', data=data)
    except urllib.error.HTTPError as e:
        e = e
        message = "天気情報の取得中にエラーがおきました。"
        return render_template('error.html', message=message, e=e)
    except:
        error_msg = "何らかのエラーが起きました。"
        return render_template('else_error.html', error_msg=error_msg)


if __name__ == "__main__":
    app.run(debug=True)
