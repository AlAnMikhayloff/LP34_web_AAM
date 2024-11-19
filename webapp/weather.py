from flask import current_app

import requests


def weather_by_city(city_name):
    weather_url = current_app.config["WEATHER_URL"]
    params = {
        'q': city_name,
        'format': 'json',
        'exclude': 'current',
        'appid': current_app.config["WEATHER_API_KEY"],
        'units': 'metric',
        'lang': 'ru',
        }
    print(weather_url)
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if 'main' and 'weather' and 'wind' in weather:
            try:
                return weather
            except (IndexError, TypeError):
                return False
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False
    return False


if __name__ == "__main__":
    print(weather_by_city("Tula,Russia"))
