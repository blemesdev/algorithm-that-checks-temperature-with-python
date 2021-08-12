from pymongo.monitoring import register
import requests
import json
import datetime
import pymongo


class Temperature:
    client = pymongo.MongoClient('localhost', 27017)
    db = client.weather
    registerdb = db.register
    daynow = datetime.datetime.now();
    temperature_now = 0
    fahrenheit = 0

    def __init__(self):
        self.temperature_now

    def get_datas(self):
        request = requests.get('https://api.hgbrasil.com/weather?woeid=456385')
        new_datas = json.loads(request.content)
        self.temperature_now = new_datas['results']['temp']
        return self.temperature_now

    def convert_temperature(self):
        self.fahrenheit = self.temperature_now * (9 / 5) + 32
        return self.fahrenheit

    def register_temperature(self):
        registro = {
            'dia': datetime.datetime.strftime(self.daynow, '%d/%m/%Y'),
            'hora': datetime.datetime.strftime(self.daynow, '%H:%M'),
            'temperatura_registrada':   self.temperature_now,
        }
        self.registerdb.insert_one(registro)
