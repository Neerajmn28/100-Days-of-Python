import requests
from datetime import datetime

TOKEN = 'ndwiciquexiieddbq34n'
USERNAME = 'neeraj28'
GRAPHID = 'graph1'
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token':TOKEN,
    'username': USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes',
}

response = requests.post(url = pixela_endpoint, json = user_params)
print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id':GRAPHID,
    'name':'Cycling Graph',
    'unit':'km',
    'type':'float',
    'color':'ajisai'
}
headers = {
    'X-USER-TOKEN': TOKEN
}


#response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
#print(response)

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}'

today = datetime.now()
print(today)




pixel_data = {
    'date':today.strftime('%Y%m%d'),
    'quantity':'10.74',
}

update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}'
new_pixel_data = {
    'quantity':'4.5',
}


response = requests.put(url = update_endpoint, json = new_pixel_data, headers = headers)
print(response.text)


#response = requests.post(url = pixel_creation_endpoint, json = pixel_data, headers = headers)
#print(response)




# delete endpoint

delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}'


response = requests.delete(url = delete_endpoint, headers = headers)
print(response.text)
