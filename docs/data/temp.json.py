import json
import sys
from helpers import get_response

data = get_response("temperature_2m")
time = data["hourly"]["time"]
temp = data["hourly"]["temperature_2m"]

data = get_response("apparent_temperature")
app_temp = data["hourly"]["apparent_temperature"]

assert len(temp) == len(app_temp), "Length mismatch between lists!"

forecast_dict = []

for i in range(len(temp)):
    forecast_dict.append({'time' : time[i],
                          'temp' : temp[i],
                          'app_temp' : app_temp[i],
                          'legend_1' : 'Air temp.',
                          'legend_2' : 'Feels like'})

json.dump(forecast_dict, sys.stdout)