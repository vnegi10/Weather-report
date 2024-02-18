import json
import sys
from helpers import get_response

data = get_response("rain")

rain = data["hourly"]["rain"]
time = data["hourly"]["time"]

forecast_dict = []

for i in range(len(rain)):
    forecast_dict.append({'time' : time[i],
                          'rain' : rain[i]})

json.dump(forecast_dict, sys.stdout)