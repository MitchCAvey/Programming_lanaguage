
import requests

# The below import will only work if you install the twilio module
# plus you will need to sign up on the twilio web site to get an
# access key to use in the API call. 
# from twilio.rest import Client

# Working with OS in python module
import os

MY_LAT = 43.472400 # Your latitude
MY_LONG = -79.682780 # Your longitude
API_KEY = ""
# api_key = os.environ.get("system_Environment_varable_Name")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
# f"https://api.openweathermap.org/data/2.5/weather?q=Oakville,Ontario&appid={api_key}"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data3 = response.json()

will_rain = False
for hour_data in weather_data3['list']:
    # print(hour_data['weather'][0])
    # print(hour_data['weather'][0]['id'])
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        # print("Bring an umbrella")
        will_rain = True
    
if will_rain:
    print("Bring an umbrella")
    # The below is for when you are using the twilio solution to 
    # send SMS messages
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body="Join Earth's mightiest heroes. Like Kevin Bacon",
    #     from='sending phone number'
    #     to="receiving phone number"
    # )
# print(message.status)

# This is my third attempt to further simplify the code
"""
weather_data2 = response.json()

# print(weather_data2['list'])

rain_code = [weather_data2["list"][len1]['weather'][len2] for len1 in range(0, len(weather_data2["list"])) for len2 in range(0, len(weather_data2["list"][len1]['weather']))]
print(rain_code)

"""

# The below is my second attempt, but this time to refine the code and simplify
"""
weather_data1 = response.json()

print(len(weather_data1["list"]))

for len1 in range(0, len(weather_data1["list"])):
    # print(len1)
    # print(weather_data["list"][len1]['weather'])
    # print(len(weather_data["list"][len1]['weather']))
    for len2 in range(0, len(weather_data1["list"][len1]['weather'])):
        print(weather_data1["list"][len1]['weather'][len2])
"""

# First attempt
"""
data = response.json()

# print(data)
for key,value in data.items():
    # print(key, value) 
    if key == 'list':
        # print(data[key]) 
        for item in data[key]:
            # print(item['weather'])
            for item2 in item['weather']:
                # print(item2)
                if item2['id'] < 700:
                    print(f"it's going to rain!!: rain code {item2['id']}")
                else:
                    print(f"It's not going to rain: rain code {item2['id']}") 

"""                    


# passed_students = {student:score for (student, score) in student_score.items() if score >= 60}
# for item in data['list']:
#     print(item['weather'])

# rain_forcast = {rain_code:value for (rain_code,value) in data.items()}
# print(rain_forcast)



