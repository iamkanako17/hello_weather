import pip._vendor.requests
import json
import urllib.request
import time
import pip._vendor.requests.api
from flask import Flask, render_template
app = Flask(__name__)

api_key = {"8cac92499bde2ad6dcf5ec1e3a1c9691"}
# api_url = "api.openweathermap.org/data/2.5/weather?lat={a}&lon={b}&appid={c}" .format(a=lat, b=lng, c=apikey)


@app.route('/')
def top_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
