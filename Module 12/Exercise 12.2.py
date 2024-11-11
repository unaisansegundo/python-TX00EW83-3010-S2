import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('API_KEY')

city = input("Enter a Spanish municipality (Example: San Sebastian or Madrid): ")
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}")
data = response.json()
print(round(data["main"]["temp"]-273.15, 1))
for weather in data["weather"]:
    print(weather['description'])