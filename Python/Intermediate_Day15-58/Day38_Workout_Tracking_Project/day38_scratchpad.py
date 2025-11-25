#! /usr/bin/python
"""
Author: Mitchell C. Avey
Creatation Date: Thursday, September 12th, 2024
Modified Date: 
"""
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth

APP_ID = ''
API_KEY = ''
BEARER_TOKEN = ""
# BEARER_HEADER = {"Authorizaation": f"Bearer {BEARER_TOKEN}"}
# bearer_headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
bearer_headers = {"Authorization": f"Bearer bearer_token-placeholder"}


EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise/'
SHEETY_GET_ENDPOINT = 'https://api.sheety.co/afbe0dfc331045fa64583e1bc072ae89/myWorkouts/workouts'

exercise_text = input("Tell me which exercises you did: ")

request_header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

request_parameters = {
    "query": exercise_text,
    "gender": 'Male',
    "weight_kg": '86.18',
    "height_cm": '177.80',
    "age": 38    
}

response1 = requests.post(EXERCISE_ENDPOINT, json=request_parameters, headers=request_header)

result1 = response1.json()

# print(result1)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result1['exercises']:
    # print(exercise)
    # print(exercise['name'])
    # print(exercise['duration_min'])
    # print(exercise['nf_calories'])
    sheet_inputs = {
        'workout': {
            'date': today_date,
            'time': now_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

print(sheet_inputs)
response2 = requests.post(SHEETY_GET_ENDPOINT, json=sheet_inputs, headers=bearer_headers)

print(response2.text)