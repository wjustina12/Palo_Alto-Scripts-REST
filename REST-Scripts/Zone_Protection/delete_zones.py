import os 
import json
import requests
import xmltodict
from rich import print as rprint 

zone_uri = "https://192.168.1.4/restapi/v10.0/Network/Zones?"
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
parameters = {'location' :'vsys', 'vsys' : "vsys1"}


def get_zone(uri, username, password, parameters):
    zone_request = requests.get(zone_uri, auth=(username,password), params=parameters, verify=False)
    zone_response = zone_request.json()
    zone_list = zone_response['result']['entry']
    
    for zone_dictionary in zone_list:
        zone_name = zone_dictionary['@name']
        rprint(f"The zones that you have available are: [green]{zone_name}[/green]")
    
    zone_deletion = input("What zone would you like to delete?\n")
    
    for zone_dictionary in zone_list:
        if zone_deletion == zone_name:
            delete_parameters = {'location' : 'vsys', 'vsys' : 'vsys1', 'name' : f'{zone_name}'}
            delete_zone(zone_uri, username, password, delete_parameters)
        else:
            rprint(f"[red]{zone_deletion}[/red] doesn't exist, please use a valid zone name.")
            rprint(zone_name)

def delete_zone(uri, username, password, zone_name, parameters):
    zone_delete_request = requests.delete(zone_uri, username, password, params=parameters, verify=False)
    zone_delete_response = zone_delete_request.json()
    rprint(zone_delete_response)
    
get_zone(zone_uri, username, password, parameters)


