import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

USERNAME = "abarragan"
TOKEN = os.getenv("PIXEL_TOKEN")


# Create A User
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# Create A Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Hours Coding",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Create a Post
today = datetime.now()

graph_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
graph_post_config = {
    "date": today.strftime("%Y%m%d"),
    "Quantity": input("How many hours did you code today?")
}

response = requests.post(url=graph_post_endpoint, json=graph_post_config, headers=headers)
print(response.text)


# Update / Delete A Post
graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20221207"
graph_update_config = {
    "quantity": "6.5"
}

# response = requests.put(url=graph_update_endpoint, json=graph_update_config, headers=headers)
# print(response.text)


# response = requests.delete(url=graph_update_endpoint, headers=headers)
# print(response.text)


