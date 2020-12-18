from flask import Flask
from flask import render_template, url_for, request
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


@app.route('/weather', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        response = request.get(weather_api)
        data = response.json()
        jsontext = json.dumps(data, indent=4)
        return render_template('weather.html', message=jsontext)
        lat = request.form['lat']
        lon = request.form['lon']
    # open weather api を叩く
    # レスポンスを受け取る
    # 多分 Binary で返ってくるので json にする
    # message に入れて html上で中身を確認する
    # 次はjsonから天気情報と都市名だけを返す
    # request.form から lat と lon をとる
    # weather_api の lat と lon を受け取った値に変える


if __name__ == "__main__":
    app.run(debug=True)
