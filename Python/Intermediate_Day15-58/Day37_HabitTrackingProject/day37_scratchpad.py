

import requests
# import datetime
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = ''
TOKEN = ''


user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# Creating a new User - use the user_parms dict
"""
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)

"""

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_id = 'graph1'

graph_config = {
    'id': graph_id,
    'name': 'Learning',
    'unit': 'completed',
    'type': 'int',
    'color': 'shibafu'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# # Creating a graph
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response)


MY_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}"

current_date = datetime.now()

formated_date = current_date.strftime("%Y%m%d")
print(formated_date)
date1 = datetime(year=2024, month=9, day=8)
print(date1.strftime("%Y%m%d"))

add_to_graph = {
    'date': formated_date,
    'quantity': '9' 
}

add_to_graph1 = {
    'date': date1.strftime("%Y%m%d"),
    'quantity': '1' 
}

# # Updating the Graph with new entries
# response1 = requests.post(url=MY_GRAPH_ENDPOINT, json=add_to_graph, headers=headers)
# print(response1.text)

update_entry = {
    'quantity': '6'
}

UPDATE_MY_GRAPH = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{formated_date}"


# # Updating an entry already on the graph
# response2 = requests.put(url=UPDATE_MY_GRAPH, json=update_entry, headers=headers)
# print(response2)

DELETE_ENTRY_ON_GRAPH = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{date1.strftime('%Y%m%d')}"

# response3 = requests.delete(url=DELETE_ENTRY_ON_GRAPH, headers=headers)
# print(response3)