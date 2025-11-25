import requests

N_POINT_API = f"https://api.npoint.io/c790b4d5cab58020d391"

class Post:
    def __init__(self):
        response = requests.get(url=N_POINT_API)
        self.post_data = response.json()
    
    def display(self):
        print(self.post_data)

    def get_all(self):
        """ Return all posts"""
        return self.post_data