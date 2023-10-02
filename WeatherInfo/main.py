import requests

from pprint import pprint

API_Key = 'ff97734a855bd586281474a6a8d0ba91'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()


pprint(weather_data)

