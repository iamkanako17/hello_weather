class Weather:
    hourly_weather = None
    hourly_temperature = None
    daily_weather = None
    current_time = None
    timezone = None
    now_temperature = None
    now_weather = None
    now_humidity = None
    now_wind = None
    now_weather_img = None

    def __init__(self, results):
        self.hourly_weather = results['hourly'][1:5]
        self.daily_weather = results['daily'][1:7]
        self.current_time = results['current']['dt']
        self.timezone = results['timezone']
        self.now_temperature = round(results['current']['temp'])
        self.now_weather = results['current']['weather'][0]['description']
        self.now_humidity = results['current']['humidity']
        self.now_wind = round(results['current']['wind_speed'])
        self.now_weather_img = results['current']['weather'][0]['icon']
