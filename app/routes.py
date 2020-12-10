from app import app
from flask import render_template, request
from app.forms import CityWeatherForm
from app.wrappers import OpenWeather


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    form = CityWeatherForm()
    city_data = None
    if request.method == 'POST' and form.validate():
        city = form.city_name.data
        weather_api = OpenWeather()
        city_data = weather_api.get_city_weather_data(city)
        print(city_data)
    return render_template('weather.html', form=form, city_data=city_data)