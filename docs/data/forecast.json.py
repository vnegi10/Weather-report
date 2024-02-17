import json
import requests as rq
import sys

# Set coordinates
long = 51.4176
lat = 5.4060

# Make a GET request via API
response = rq.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m")
if response.status_code == 200:
    data = response.json()
else:
    print(f"Failed to fetch data, check status code {response.status_code}")

temp = data["hourly"]["temperature_2m"]
time = data["hourly"]["time"]

forecast_dict = []

for i in range(len(temp)):
    forecast_dict.append({'time' : time[i],
                          'temp' : temp[i]})

json.dump(forecast_dict, sys.stdout)