from flask import Flask, render_template, url_for, requests, json, os
# from jinja2 import Template, Environment, FileSystemLoader

app = Flask(__name__)
geo_key = "AIzaSyDyR6n90hQQiz88u3JeWO8dwC4Cbjzmnb8"
weather_key = "8cac92499bde2ad6dcf5ec1e3a1c9691"
weather_api= "http://api.openweathermap.org/data/2.5/weather?lat={a}&lon={b}&appid={c}" .format(a=lat, b=lng, c=weather_key)


@app.route('/')
def index():
    render_template("index.html")

if __name__ == "__main__":
    app.run()
