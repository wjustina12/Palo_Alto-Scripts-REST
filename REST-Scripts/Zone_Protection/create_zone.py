import os 
import json
import requests 
import xmltodict
from rich import print as rprint 

zone_uri = "https://192.168.1.4/restapi/v10.0/Network/Zones"
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

def create_zone(uri, username, password):
    name = input("What would you like to name the zone?\n")
    user_id = input("Would you like User-ID enabled on this zone? (Yes or No)\n")
    device_id = input("Would you like Device ID enabled on this zone? (Yes or No)")
    network_type = input("What type of zone is this? (Virtual-Wire, Tap, Layer 2, Layer 3, External, or Tunnel?")
    interface = input("What interface will this security zone be assigned to? (Example: Ethernet1")
    zone_create_body = {
        "entry" : {
            "@name" : name, 
            "enable-user-identification" : user_id,
            "enable-device-identification" : device_id, 
            "network" : {
                network_type : {
                    "member" : []
                }
            }
        }
    }
    zone_request = requests.post(uri, auth=(username,password), verify=False)