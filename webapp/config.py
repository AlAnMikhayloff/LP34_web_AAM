import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = "Tula,Russia"
WEATHER_API_KEY = "6af8009901fa457cee756d7b0a5a09c8"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..',
                                                      'webapp.db',
                                                      )
SECRET_KEY = "owirhOIiHvioOIo*&KHUIHtKJHG)OIhuyut>?<MuhuYGBKJH^^%&^"
REMEMBER_COOKIE_DURATION = timedelta(days=5)
SQLALCHEMY_TRACK_MODIFICATIONS = False
