

import requests

MY_LAT = 51.253777
MY_LNG = -85.323212

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()


"""
Basic structure to making API Calls
"""
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# iss_position = (longitude, latitude)

# print(iss_position)