import requests as rq

# Set coordinates for Veldhoven
lat = 5.4060
long = 51.4176

URL = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly="

# Make a HTTP GET request to Open-Meteo API
def get_response(endpoint):
    # Make a GET request via API
    url = "".join((URL, endpoint))
    response = rq.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data, check status code {response.status_code}")