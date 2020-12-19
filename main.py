from flask import Flask
from flask import render_template, url_for, request
import urllib.request
import json
import os

app = Flask(__name__)
api_key = os.environ.get('WEATHER_KEY')
lat = 35
lon = 139
weather_api = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/weather', methods=['GET'])
def weather():
    req = urllib.request.Request(weather_api)
    with urllib.request.urlopen(req) as res:
        body = res.read()

    return render_template('weather.html', message=body)

# @app.route('/weather/<userlocation>', method=['POST'])
# def location(userlocation):
#     data = request.get_json()
#     return "{}, {}" .format(data["weather"], data["name"])

    # lat = request.form['lat']
    # lon = request.form['lon']
    # open weather api を叩く [完了]
    # レスポンスを受け取る [完了]
    # 多分 Binary で返ってくるので json にする [完了]
    # message に入れて html上で中身を確認する [完了]

    # 次はjsonから天気情報と都市名だけを返す 
    # request.form から lat と lon をとる
    # weather_api の lat と lon を受け取った値に変える

@app.route('/weather/info', methods=['GET'])
def get_weather():
    data = {
        "weather": [{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],
        "id" : "1851632"
    }

    req = urllib.request.Request(weather_api, json.dumps(data))
    with urllib.request.urlopen(req) as res:
        body = res.read()



if __name__ == "__main__":
    app.run(debug=True)
