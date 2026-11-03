from threading import Thread
import requests
from weather import Weather

class WeatherGetter(Thread):
    def __init__(self):
        Thread.__init__(self)
        global CITIES
        global reports
        print(CITIES)
    def run(self):
        while len(CITIES)>=0:
            self.city = CITIES.pop()
            url_template = (
                'http://api.openweathermap.org/data/2.5/'
                'weather?q={}&units={}&APPID=48f2d5e18b0d2bc50519b58cce6409f1')
            response = requests.get(url_template.format(self.city, 'metric'))
            data = response.json() # json.loads(response.text)
            self.temperature = data['main']['temp']
            self.description = data['weather'][0]['description']
            weather = Weather(city=self.city, temperature=self.temperature, desc=self.description)
            reports.push(weather)
