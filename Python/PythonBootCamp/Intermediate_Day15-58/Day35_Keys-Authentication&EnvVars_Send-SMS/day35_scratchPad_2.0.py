import requests
from twilio.rest import Client
import os


MY_LAT = 43.472400 # Your latitude
MY_LONG = -79.682780 # Your longitude
API_KEY = ""
# API_KEY = os.environ.get("OWM_API_KEY")
account_sid = ''
auth_token = ''
# auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

"""
NOTE: for the above global variables that are commented out, you'll have to create System Environment Variables
to have those 
"""

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'cnt': 4   
}

will_rain = False

response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()

forcast_data = response.json()

# print(forcast_data['list'])

for hourly_data in forcast_data['list']:
    # print(hourly_data['weather'][0]['id'])
    twelve_hour_forcast = hourly_data['weather'][0]['id']
    if int(twelve_hour_forcast) < 700:
        # print("you need an umbrella")
        will_rain = True
    # else: 
        # print("No umbrella is needed")

if will_rain:
    # print("you need an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12294596079', 
        to='+16475265771',
        body="It's going to rain today. Remember to bring an Umbrella"
        )

    print(message.status)
