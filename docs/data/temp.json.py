import json
import sys
from helpers import get_response

data = get_response("temperature_2m")

temp = data["hourly"]["temperature_2m"]
time = data["hourly"]["time"]

forecast_dict = []

for i in range(len(temp)):
    forecast_dict.append({'time' : time[i],
                          'temp' : temp[i]})

json.dump(forecast_dict, sys.stdout)