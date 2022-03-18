import os 
import json 
import xmltodict
import requests
from rich import print as rprint 

zone_uri = "https://192.168.1.4/restapi/v10.0/Network/Zones?"
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
parameters = {'location' :'vsys', 'vsys' : "vsys1"}

def get_zone(uri, username, password, parameters):
    zone_request = requests.get(zone_uri, auth=(username,password), params=parameters, verify=False)
    zone_response = zone_request.json()
    rprint(zone_response)

get_zone(zone_uri, username, password, parameters)