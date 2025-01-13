import requests
from datetime import datetime
USERNAME = ""
TOKEN = ""
GRAPH_ID = ""
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
	"token": "",
	"username": "",
	"agreeTermsOfService": "",
	"notMinor": "",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
	"id": GRAPH_ID,
	"name": "Cycling Graph",
	"unit": "km",
	"type": "float", #if the type is integer the quantity is going to be a whole number.
	"color": "ajisai"
}

headers = {
	"X-USER-TOKEN": TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today)

pixel_data = {
	"date": today.strftime("%Y%m%d"),
	"quantity": input("How many kilometers did you cycle today? ")
}

#https://pixe.la/v1/users/ayanfe/graphs/graph1.html

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
	"quantity": "26.45"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# If you want to delete the former result
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)