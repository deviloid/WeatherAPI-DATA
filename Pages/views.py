from django.shortcuts import render
import requests

key = '053bec05e35944f4808215348212106'
url = 'http://api.weatherapi.com/v1/current.json?key={}&q={}'

# Create your views here.
def home(request, location):

    q = location

    city_weather = requests.get(url.format(key, q)).json()

    weather = {
        'city' : city_weather['location']['name'],
        'temperature' : city_weather['current']['temp_f'],
        'description' : city_weather['current']['condition']['text'],
        'icon' : city_weather['current']['condition']['icon']
    }
    
    context = {
        'weather' : weather
    }

    return render(request, 'Pages/home.html', context)