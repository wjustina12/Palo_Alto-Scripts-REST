import os 
import json
import requests
from rich import print as rprint 

zone_protection_uri = 'https://192.168.1.4/restapi/v10.0/Network/ZoneProtectionNetworkProfiles?'
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

class ZoneProtection:
    def __init__(self, uri, username, password):
        self.uri = uri
        self.username = username
        self.password = password

    def retrieve_profile(self):
        zone = requests.get(self.uri, auth=(self.username, self.password), verify=False)
        zone_response = zone.json()
        rprint(zone_response)
    
    def create_profile(self, profile_name):
        zone_body = {
            "entry" : {
                "@name" : profile_name,
                "description" : input("What description would you like on this profile?"), 
                "scan" : {
                    "entry" : [
                        {
                            "@name" : "TCP Port Scan", 
                            "action" : {
                            "deny" : {}, 
                            "interval" : 2,
                            "threshold" : 50
                            }
                        }, 
                        {
                            "@name" : "Host Sweep", 
                            "action" : {
                            "deny" : {}, 
                            "interval" : 2,
                            "threshold" : 50
                            }
                        }, 
                        {
                            "@name" : "UDP Port Scan", 
                            "action" : {
                            "deny" : {}, 
                            "interval" : 2,
                            "threshold" : 50
                            }
                        }
                    ]
                },
                "scan-white-list" : {
                    "entry": [
                        {"ipv4" : "192.168.1.3"}
                    ]
                },
                "flood" : {
                    "tcp-syn" : {
                        "red" : {
                            "alarm-rate" : 500, 
                            "activate-rate" : 600, 
                            "maximal-rate" : 750
                        }
                    }, 
                    "udp" : {
                        "enable" : "yes"
                        }
                }
            }
        }
        zone = requests.post(self.uri, auth=(self.username, self.password), verify=False, data=)

        
def get_protection_zone(uri):
    zone = requests.get(uri, auth=(username,password), verify=False)
    zone_response = zone.json()
    rprint(zone_response)

firewall = ZoneProtection(zone_protection_uri, username, password)
firewall.retrieve_profile()