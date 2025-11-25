import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)

if response.status_code != 200:
    raise Exception("Bad response from ISS API")

if response.status_code == 404:
    raise Exception("That resource does not exist!")
elif response.status_code == 401:
    raise Exception("You are not authorised to access this data!")

response.raise_for_status()

data = response.json()
print(data)
print(data['iss_position']) 

data2 = response.json()['iss_position']
print(data2)

data3 = response.json()['iss_position']['longitude']
print(data3)