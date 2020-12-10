import requests
from datetime import datetime


class CityWeather:
    def __init__(self, city, current, hi, lo, feels_like, description, sunrise, sunset):
        self.city = city
        self.current = current
        self.hi = hi
        self.lo = lo
        self.feels_like = feels_like
        self.description = description
        self.sunrise = sunrise
        self.sunset = sunset

    def __str__(self):
        return f"City Weather: {self.city}"

    def __repr__(self):
        return f"<City Weather | {self.city}>"


class OpenWeather:
    def __init__(self):
        self.base_path = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = {"YOUR-API-KEY"}

    def get_city_weather_data(self, city):
        url = self.base_path + "?q=" + city + "&appid=" + self.api_key + "&units=imperial"
        r = requests.get(url)
        response = r.json()
        city = response['name']
        current = response['main']['temp']
        hi = response['main']['temp_max']
        lo = response['main']['temp_min']
        feels_like = response['main']['feels_like']
        description = response['weather'][0]['description']
        sunrise = datetime.fromtimestamp(response['sys']['sunrise'])
        sunset = datetime.fromtimestamp(response['sys']['sunset'])
        city_data = CityWeather(city, current, hi, lo, feels_like, description, sunrise, sunset)
        return city_data