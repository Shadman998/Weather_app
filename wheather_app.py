import requests
from pprint import pprint

city=input("enter any city name:")

API_KEY="e25033e7ebcf723100aebf163025aaa8"

url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,API_KEY)

weather=requests.get(url).json()

pprint(weather)