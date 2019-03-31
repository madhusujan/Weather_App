import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm 

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=d78955a59874d2dfb64fe5b7f3c7a8a5'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm() 

    cities = City.objects.all()
 
    weather_data = []
 

    for city in cities:
            r = requests.get(url.format(city)).json()

            city_weather = {
                'city' : city.name,
                'temperature' : r['main']['temp'] ,
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
            }

            weather_data.append(city_weather)
            
    print(weather_data)

    context = {'weather_data' : weather_data, 'form' : form}
    return render( request, 'weather/weather.html',  context)

    # {"coord":{"lon":-74.17,"lat":40.74},"weather":[
    #     {"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}]
    #     ,"base":"stations","main":{"temp":57.2,
    #     "pressure":1012,"humidity":42,"temp_min":50,
    #     "temp_max":63},"visibility":16093,
    #     "wind":{"speed":12.75,"deg":180},
    #     "clouds":{"all":75},"dt":1554000960,
    #     "sys":{"type":1,"id":4026,"message":0.0083,
    #     "country":"US","sunrise":1553942625,
    #     "sunset":1553987902},"id":5101798,
    #     "name":"Newark","cod":200}