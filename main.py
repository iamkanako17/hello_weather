from flask import Flask
from flask import render_template, url_for, request
import urllib.request, json
import urllib.parse
import os

app = Flask(__name__)
api_key = os.environ.get('WEATHER_KEY')
#  ファイルにするのか
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
        results = json.loads(body)
        name = results["name"]
        weather = results["weather"]
        geo = results["coord"]
        city_id = results["id"]
        img = weather[0]['icon']
        api_str = f"http://api.openweathermap.org/data/2.5/weather?lat={geo['lat']}&lon={geo['lon']}&appid={api_key}"
    return render_template('weather.html', name=name, wet=weather, geo=geo, id=city_id, img=img)

    # open weather api を叩く [完了]
    # レスポンスを受け取る [完了]
    # 多分 Binary で返ってくるので json にする [完了]
    # message に入れて html上で中身を確認する [完了]

    # 次はjsonから天気情報と都市名だけを返す 
    # request.form から lat と lon をとる
    # weather_api の lat と lon を受け取った値に変える


if __name__ == "__main__":
    app.run(debug=True)
