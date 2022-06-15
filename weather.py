import requests
from ss import *


api_address ='' + key
json_data = requests.get(api_address).json()



def temp():
    temperature = round(json_data['main']['temperature']-273,1)
    return temperature

def des():
    description = json_data['weather'][0]['description']
    return description

